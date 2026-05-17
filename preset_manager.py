##############################################################################################################################################
#
# preset_manager.py — Gerenciador de presets para Nano Cortex
#
# COMO EDITAR:
#   Cada entrada em PRESETS representa um preset da Nano Cortex.
#   A chave é o número do Program Change (0-based, igual ao que a Nano Cortex recebe).
#
#   Campos:
#     "name"  : Nome exibido no display central ao selecionar o preset
#     "fx"    : Estado inicial de cada efeito ao entrar no preset
#                 Chave  = número do CC
#                 Valor  = True (efeito LIGADO) ou False (efeito DESLIGADO)
#
#   CCs da Nano Cortex:
#     34 = INPUT GATE
#     37 = FX Slot 1
#     38 = FX Slot 2
#     39 = FX Slot 3
#     40 = FX Slot 4
#     41 = FX Slot 5
#
##############################################################################################################################################

PRESETS = {
    #      name           Gate   FX1    FX2    FX3    FX4    FX5
    0:  { "name": "Preset 1",  "fx": { 34: False, 37: False, 38: False, 39: False, 40: False, 41: False } },
    1:  { "name": "Preset 2",  "fx": { 34: False, 37: True,  38: False, 39: False, 40: False, 41: False } },
    2:  { "name": "Preset 3",  "fx": { 34: False, 37: True,  38: True,  39: False, 40: False, 41: False } },
    3:  { "name": "Preset 4",  "fx": { 34: False, 37: False, 38: False, 39: True,  40: True,  41: False } },
    4:  { "name": "Preset 5",  "fx": { 34: False, 37: False, 38: False, 39: False, 40: True,  41: True  } },
    5:  { "name": "Preset 6",  "fx": { 34: True,  37: False, 38: False, 39: False, 40: False, 41: False } },
    6:  { "name": "Preset 7",  "fx": { 34: False, 37: True,  38: False, 39: True,  40: False, 41: False } },
    7:  { "name": "Preset 8",  "fx": { 34: False, 37: False, 38: True,  39: False, 40: True,  41: False } },
    8:  { "name": "Preset 9",  "fx": { 34: False, 37: False, 38: False, 39: False, 40: False, 41: False } },
    9:  { "name": "Preset 10", "fx": { 34: False, 37: True,  38: False, 39: False, 40: False, 41: False } },
    10: { "name": "Preset 11", "fx": { 34: False, 37: False, 38: True,  39: False, 40: False, 41: False } },
    11: { "name": "Preset 12", "fx": { 34: False, 37: False, 38: False, 39: True,  40: False, 41: False } },
    12: { "name": "Preset 13", "fx": { 34: False, 37: False, 38: False, 39: False, 40: True,  41: False } },
    13: { "name": "Preset 14", "fx": { 34: False, 37: False, 38: False, 39: False, 40: False, 41: True  } },
    14: { "name": "Preset 15", "fx": { 34: True,  37: True,  38: False, 39: False, 40: False, 41: False } },
    15: { "name": "Preset 16", "fx": { 34: False, 37: True,  38: True,  39: True,  40: False, 41: False } },
    16: { "name": "Preset 17", "fx": { 34: False, 37: False, 38: False, 39: False, 40: False, 41: False } },
    17: { "name": "Preset 18", "fx": { 34: False, 37: True,  38: False, 39: False, 40: False, 41: False } },
    18: { "name": "Preset 19", "fx": { 34: False, 37: False, 38: True,  39: False, 40: False, 41: False } },
    19: { "name": "Preset 20", "fx": { 34: False, 37: False, 38: False, 39: True,  40: False, 41: False } },
    20: { "name": "Preset 21", "fx": { 34: False, 37: False, 38: False, 39: False, 40: True,  41: False } },
    21: { "name": "Preset 22", "fx": { 34: False, 37: False, 38: False, 39: False, 40: False, 41: True  } },
    22: { "name": "Preset 23", "fx": { 34: True,  37: True,  38: True,  39: False, 40: False, 41: False } },
    23: { "name": "Preset 24", "fx": { 34: False, 37: True,  38: True,  39: True,  40: True,  41: False } },
    24: { "name": "Preset 25", "fx": { 34: False, 37: False, 38: False, 39: False, 40: False, 41: False } },
    25: { "name": "Preset 26", "fx": { 34: False, 37: True,  38: False, 39: False, 40: False, 41: False } },
    26: { "name": "Preset 27", "fx": { 34: False, 37: False, 38: True,  39: False, 40: False, 41: False } },
    27: { "name": "Preset 28", "fx": { 34: False, 37: False, 38: False, 39: True,  40: False, 41: False } },
    28: { "name": "Preset 29", "fx": { 34: False, 37: False, 38: False, 39: False, 40: True,  41: False } },
    29: { "name": "Preset 30", "fx": { 34: False, 37: False, 38: False, 39: False, 40: False, 41: True  } },
    30: { "name": "Preset 31", "fx": { 34: True,  37: False, 38: True,  39: False, 40: True,  41: False } },
    31: { "name": "Preset 32", "fx": { 34: True,  37: True,  38: True,  39: True,  40: True,  41: True  } },
}

##############################################################################################################################################
# Implementação interna
##############################################################################################################################################

from pyswitch.controller.actions import Action
from adafruit_midi.midi_message import MIDIMessage
from display import DISPLAY_PRESET_NAME as _DISPLAY_PRESET_NAME


class _RawMessage(MIDIMessage):
    def __init__(self, data):
        self.__data = bytearray(data)
    def __bytes__(self):
        return self.__data


class _SharedState:
    current_pc       = -1
    fx_states        = {}
    appl             = None
    preset_callbacks = []
    fx_callbacks     = {}

_state = _SharedState()


class _BaseCallback:
    def __init__(self):
        self.action = None

    def init(self, appl, listener=None):
        self._appl = appl

    def reset(self):
        pass

    def push(self):
        pass

    def release(self):
        pass

    def update_displays(self):
        pass


# ── Preset callback ────────────────────────────────────────────────────────────

class _PresetCallback(_BaseCallback):
    def __init__(self, pc, channel, color, text):
        super().__init__()
        self._pc      = pc
        self._channel = channel
        self._color   = color
        self._text    = text
        _state.preset_callbacks.append(self)

    def init(self, appl, listener=None):
        self._appl = appl
        _state.appl = appl

    def _set_led(self):
        is_active = (_state.current_pc == self._pc)
        self.action.switch.color      = self._color
        self.action.switch.brightness = 1.0 if is_active else 0.05

    def push(self):
        self._appl.client.midi.send(_RawMessage([0xC0 | self._channel, self._pc]))
        _state.current_pc = self._pc
        preset = PRESETS.get(self._pc, {})
        # Atualiza nome no display central
        _DISPLAY_PRESET_NAME.text = preset.get("name", "")
        # Atualiza estados dos efeitos
        for cc, active in preset.get("fx", {}).items():
            _state.fx_states[cc] = active
        # Atualiza LEDs: enabled → framework, disabled → direto no switch
        for cb in _state.preset_callbacks:
            if cb.action.enabled:
                cb.action.update_displays()
            else:
                cb._set_led()
        for cb in _state.fx_callbacks.values():
            if cb.action.enabled:
                cb.action.update_displays()
            else:
                cb._set_led()

    def update_displays(self):
        if self.action.label:
            self.action.label.text       = self._text
            self.action.label.back_color = self._color
        if not self.action.enabled:
            return
        is_active = (_state.current_pc == self._pc)
        self.action.switch_color      = self._color
        self.action.switch_brightness = 1.0 if is_active else 0.05


# ── FX callback ────────────────────────────────────────────────────────────────

class _FxCallback(_BaseCallback):
    def __init__(self, cc, channel, color_on, color_off, text):
        super().__init__()
        self._cc        = cc
        self._channel   = channel
        self._color_on  = color_on
        self._color_off = color_off
        self._text      = text
        _state.fx_states.setdefault(cc, False)
        _state.fx_callbacks[cc] = self

    def _set_led(self):
        active = _state.fx_states.get(self._cc, False)
        self.action.switch.color      = self._color_on if active else self._color_off
        self.action.switch.brightness = 1.0 if active else 0.05

    def push(self):
        new_state = not _state.fx_states.get(self._cc, False)
        _state.fx_states[self._cc] = new_state
        self._appl.client.midi.send(_RawMessage([0xB0 | self._channel, self._cc, 127 if new_state else 0]))
        self._set_led()
        # Atualiza o label do header
        active = new_state
        color  = self._color_on if active else self._color_off
        if self.action.label:
            self.action.label.text       = self._text
            self.action.label.back_color = color

    def update_displays(self):
        active = _state.fx_states.get(self._cc, False)
        color  = self._color_on if active else self._color_off
        if self.action.label:
            self.action.label.text       = self._text
            self.action.label.back_color = color
        if not self.action.enabled:
            return
        self.action.switch_color      = color
        self.action.switch_brightness = 1.0 if active else 0.05


# ── API pública ────────────────────────────────────────────────────────────────

def PRESET_SELECT(pc, channel=0, color=(255, 255, 255), display=None, text="", id=None, enable_callback=None):
    return Action({
        "callback":       _PresetCallback(pc=pc, channel=channel, color=color, text=text),
        "display":        display,
        "useSwitchLeds":  True,
        "id":             id,
        "enableCallback": enable_callback,
    })


def EFFECT_TOGGLE(cc, channel=0, color_on=(190, 10, 90), color_off=(0, 0, 0), display=None, text=""):
    return Action({
        "callback":      _FxCallback(cc=cc, channel=channel, color_on=color_on, color_off=color_off, text=text),
        "display":       display,
        "useSwitchLeds": True,
    })
