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
  - 4-page navigation (A/B/C/D) with UP/DOWN switches, giving access to 32 presets
  - Per-preset FX state definition (which effects are on/off when a preset loads)
  - Direct NeoPixel LED control, bypassing the pyswitch segment system to avoid conflicts between actions sharing the same physical switch
  - **Tap Tempo** mode with visual BPM feedback on the display and pulsing LED
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
| UP | Go to previous page (A→D wraps) | Enter **Tap Tempo mode** |
| DOWN | Go to next page (D→A wraps) | Toggle FX Slot 5 (CC#41) |

### Preset Pages

| Page | Presets |
|---|---|
| A | 1 – 8 (PC 0–7) |
| B | 9 – 16 (PC 8–15) |
| C | 17 – 24 (PC 16–23) |
| D | 25 – 32 (PC 24–31) |

### LED Colors

| Color | Meaning |
|---|---|
| Cyan (bright) | Active preset |
| White (dim) | Inactive preset |
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

Edit the `PRESETS` dictionary at the top of `preset_manager.py`:

```python
PRESETS = {
    0:  { "name": "Clean",  "fx": { 34: False, 37: False, 38: True,  39: False, 40: True,  41: True  } },
    1:  { "name": "Crunch", "fx": { 34: True,  37: True,  38: False, 39: False, 40: True,  41: False } },
    2:  { "name": "Lead",   "fx": { 34: True,  37: True,  38: True,  39: True,  40: True,  41: True  } },
    # ... up to preset 31
}
```

- The **key** is the PC number (0-based, matching what the Nano Cortex receives)
- `"name"` is shown in the center display when the preset is selected
- `"fx"` defines which FX slots should be on (`True`) or off (`False`) when the preset loads — this is tracked locally, since the Nano Cortex does not send state back over TRS

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

- The Nano Cortex **only outputs MIDI feedback via USB**, not TRS. This means the controller cannot receive preset names or FX states from the amp — all state is managed locally based on what you define in `PRESETS`.
- If you need bidirectional communication (so the controller always reflects the true state of the Nano Cortex), a computer running a MIDI bridge script (`midi_bridge.py`, included) can route USB MIDI between the two devices.
- This project was built and tested with the **MIDI Captain 10**. Other MIDI Captain models would require changes to `inputs.py` and the hardware device imports.

---

## License

This project builds on [pyswitch](https://github.com/Tunetown/PySwitch) which is licensed under MIT. All additions in this repository follow the same license.
