# captain-cortex

A custom firmware for the **PaintAudio MIDI Captain 10** foot controller, designed to control the **Neural DSP Nano Cortex** amp modeler via standard MIDI (TRS cable).

Built on top of the [pyswitch](https://github.com/Tunetown/PySwitch) framework by Tunetown.

---

## What is this?

The MIDI Captain 10 is a powerful 10-switch MIDI foot controller running CircuitPython on a Raspberry Pi Pico (RP2040). It was originally designed to work with the **Kemper Profiler** through a proprietary bidirectional SysEx protocol.

captain-cortex adapts this controller to work with the **Neural DSP Nano Cortex**, which communicates via standard MIDI (Program Change and Control Change messages) over a TRS cable. Since the Nano Cortex only sends feedback via USB (not TRS), the controller operates in a **one-way communication mode** — all state (active preset, FX on/off) is tracked locally on the MIDI Captain itself.

---

## Hardware Requirements

| Device | Role |
|---|---|
| PaintAudio MIDI Captain 10 | MIDI foot controller |
| Neural DSP Nano Cortex | Amp modeler / cab simulator / effects processor |
| TRS-MIDI cable (Type A or B) | Connection between the two devices |

The Nano Cortex TRS MIDI input receives Program Change and Control Change messages from the MIDI Captain.

---

## Key Changes from the Original pyswitch Setup

### Removed
- **Kemper bidirectional protocol** (`KemperBidirectionalProtocol`) — the Nano Cortex does not speak Kemper SysEx
- **`KemperRigNameCallback`** and **`TunerDisplayCallback`** — replaced with static display labels updated locally
- **`BidirectionalProtocolState`** dot indicator — not applicable without bidirectional communication
- **`PagerAction`** from pyswitch — replaced with a custom paging system that has full, direct LED control

### Added
- **`preset_manager.py`** — a complete custom preset and paging system built from scratch, including:
  - Up to 8 pages (A–H) of navigation with UP/DOWN switches, giving access to up to 64 presets — page count adjusts automatically based on how many presets are defined
  - Per-preset FX state definition (which effects are on/off when a preset loads)
  - Direct NeoPixel LED control, bypassing the pyswitch segment system to avoid conflicts between actions sharing the same physical switch
  - Empty preset slots (no name defined) have their LED turned off and button blocked — no MIDI is sent
  - **Tap Tempo** mode with visual BPM feedback on the display and pulsing LED
- **`presets.py`** — separate file for preset configuration, easy to read and edit
- **`preset_editor.html`** — browser-based visual editor for `presets.py` (see below)
- **`DISPLAY_PAGER`** label — shows current page and active preset reference (e.g. `A3 - 3`)
- **`DISPLAY_PRESET_NAME`** label — shows the name of the active preset in large text

---

## Display Layout

```
┌─────────────────────────────────────┐
│  GATE  │  FX 1  │  FX 2  │  (30px) │  ← FX status headers (row 1)
│  FX 3  │  FX 4  │  FX 5  │  (30px) │  ← FX status headers (row 2)
│                                     │
│           Preset Name               │  ← Large preset name (120px)
│                                     │
│         A3 - 3  (white bg)          │  ← Pager label (60px)
└─────────────────────────────────────┘
```

---

## Switch Layout & Functions

```
┌─────┬─────┬─────┬─────┬──────┐
│  1  │  2  │  3  │  4  │  UP  │
├─────┼─────┼─────┼─────┼──────┤
│  A  │  B  │  C  │  D  │ DOWN │
└─────┴─────┴─────┴─────┴──────┘
```

### Normal Mode

| Switch | Press | Hold |
|---|---|---|
| 1 | Select preset slot 1 of current page | Toggle INPUT GATE (CC#34) |
| 2 | Select preset slot 2 of current page | — |
| 3 | Select preset slot 3 of current page | — |
| 4 | Select preset slot 4 of current page | — |
| A | Select preset slot 5 of current page | Toggle FX Slot 1 (CC#37) |
| B | Select preset slot 6 of current page | Toggle FX Slot 2 (CC#38) |
| C | Select preset slot 7 of current page | Toggle FX Slot 3 (CC#39) |
| D | Select preset slot 8 of current page | Toggle FX Slot 4 (CC#40) |
| UP | Go to previous page (wraps A↔H) | Enter **Tap Tempo mode** |
| DOWN | Go to next page (wraps H↔A) | Toggle FX Slot 5 (CC#41) |

### Preset Pages

Pages are assigned automatically based on the number of presets defined in `presets.py`. Each page holds 8 preset slots:

| Page | Presets |
|---|---|
| A | 1 – 8 (PC 0–7) |
| B | 9 – 16 (PC 8–15) |
| C | 17 – 24 (PC 16–23) |
| D | 25 – 32 (PC 24–31) |
| E | 33 – 40 (PC 32–39) |
| F | 41 – 48 (PC 40–47) |
| G | 49 – 56 (PC 48–55) |
| H | 57 – 64 (PC 56–63) |

### LED Colors

| Color | Meaning |
|---|---|
| Cyan (bright) | Active preset |
| White (dim) | Inactive preset slots |
| Black (off) | Empty slot — no preset defined |
| Magenta/Pink (bright) | FX slot active |
| Black (off) | FX slot inactive |

---

## Tap Tempo Mode

Hold **Switch UP** for ~600ms to enter Tap Tempo mode:

- All preset and FX LEDs turn off
- Switch UP: one LED lights up in **pink** — indicates tap mode is active
- Switch DOWN: **pulses in cyan** at the current BPM
- Display shows `TAP` (before first tap) or the calculated BPM (e.g. `127 BPM`)
- Tap Switch DOWN to the beat — after the second tap, BPM is calculated and sent as **CC#42** to the Nano Cortex
- Press Switch UP to exit tap mode and return to normal

---

## Nano Cortex MIDI CC Map

| CC | Function |
|---|---|
| CC#34 | INPUT GATE bypass (0–63 = Off, 64–127 = On) |
| CC#37 | FX Slot 1 bypass |
| CC#38 | FX Slot 2 bypass |
| CC#39 | FX Slot 3 bypass |
| CC#40 | FX Slot 4 bypass |
| CC#41 | FX Slot 5 bypass |
| CC#42 | Tap Tempo |

---

## Configuring Your Presets

### Using the visual editor (recommended)

Open `preset_editor.html` in any browser — no server needed, works directly from the file system.

The editor lets you:
- **Name** each preset slot
- **Toggle** each FX slot on or off per preset
- **Import** an existing `presets.py` to continue editing it
- **Download** the generated `presets.py` ready to copy to the device
- Session is **automatically saved** in the browser — your work is preserved between visits

Empty slots (no name) are not generated in the output file. On the device, their LED is off and the button does nothing.

### Editing presets.py manually

Presets are defined in `presets.py`. Each preset takes two lines — the name on one line and the FX states on the next, making it easy to edit without breaking column alignment:

```python
_PRESETS_RAW = [

    # ── Page A ──────────────────────────────────────────────────────────────
    #            gate   fx1    fx2    fx3    fx4    fx5

    (  0, "Clean",
         _OFF,  _OFF,  _OFF,  _OFF,  _ON,   _ON   ),

    (  1, "Crunch",
         _ON,   _ON,   _OFF,  _OFF,  _ON,   _OFF  ),
]
```

- The first value is the PC number (0-based)
- `_ON` / `_OFF` map to FX slots: Gate, FX1, FX2, FX3, FX4, FX5
- The number of pages adjusts automatically — no need to configure anything else
- Slots left undefined will have their LED off and button disabled on the device

---

## Installing

1. Connect the MIDI Captain to your computer via USB while holding **Switch 1 (GP1)** — a drive will appear on your computer
2. Copy all project files into the root of that drive:
   - `code.py`, `boot.py`, `config.py`, `communication.py`, `display.py`, `inputs.py`
   - `preset_manager.py`, `presets.py`
   - The entire `lib/` folder
3. Eject the drive and reconnect normally — the firmware will start automatically

---

## Mounting the USB Drive (for editing files)

By default, the USB drive is hidden during normal operation. To mount it for editing:

1. Disconnect USB
2. Hold **Switch 1 (GP1)**
3. Reconnect USB while holding the switch
4. The `CIRCUITPY` drive will appear on your computer
5. Edit your files, eject safely, and reconnect normally

---

## Project Structure

```
captain-cortex/
├── code.py              # Entry point — starts pyswitch
├── boot.py              # Boot config — USB drive toggle
├── config.py            # pyswitch runtime config
├── communication.py     # MIDI routing (TRS only, no Kemper protocol)
├── display.py           # Display layout and label definitions
├── inputs.py            # Switch assignments
├── preset_manager.py    # Custom paging, preset selection, FX toggles, tap tempo
├── presets.py           # Preset definitions — edit this to configure your presets
├── preset_editor.html   # Visual browser-based preset editor
├── gerar_boot.py        # Helper script to regenerate logo.bmp on Windows
└── lib/                 # CircuitPython libraries (pyswitch, adafruit_midi, etc.)
```

---

## Dependencies

- [CircuitPython 7.3.1](https://circuitpython.org/board/raspberry_pi_pico/) — for the Raspberry Pi Pico
- [pyswitch](https://github.com/Tunetown/PySwitch) — MIDI controller framework (included in `lib/`)
- Adafruit CircuitPython libraries (included in `lib/`)

---

## Notes

- The Nano Cortex **only outputs MIDI feedback via USB**, not TRS. This means the controller cannot receive preset names or FX states from the amp — all state is managed locally based on what you define in `presets.py`.
- If you need bidirectional communication (so the controller always reflects the true state of the Nano Cortex), a computer running a MIDI bridge script (`midi_bridge.py`, included) can route USB MIDI between the two devices.
- This project was built and tested with the **MIDI Captain 10**. Other MIDI Captain models would require changes to `inputs.py` and the hardware device imports.

---

## License

This project builds on [pyswitch](https://github.com/Tunetown/PySwitch) which is licensed under MIT. All additions in this repository follow the same license.
