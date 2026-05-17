##############################################################################################################################################
#
# preset_manager.py — Gerenciador de presets para Nano Cortex
#
# COMO EDITAR:
#   Cada entrada em PRESETS representa um preset da Nano Cortex.
#   A chave é o número do Program Change (0-based, igual ao que a Nano Cortex recebe).
#
#   Campos:
#     "name"  : Nome do preset (uso futuro no display)
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
# EXEMPLO:
#   0: { "name": "Clean",  "fx": { 34: False, 37: False, 38: True,  39: False, 40: True,  41: True  } },
#   1: { "name": "Crunch", "fx": { 34: True,  37: True,  38: False, 39: False, 40: True,  41: False } },
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
# Implementação interna — não é necessário editar abaixo desta linha.
##############################################################################################################################################

from pyswitch.controller.callbacks import Callback
from pyswitch.controller.actions import Action
from adafruit_midi.midi_message import MIDIMessage


class _RawMessage(MIDIMessage):
    def __init__(self, data):
        self.__data = bytearray(data)
    def __bytes__(self):
        return self.__data


# Estado global compartilhado entre todos os callbacks
class _SharedState:
    current_pc       = -1   # PC do preset ativo (-1 = nenhum)
    fx_states        = {}   # { cc: bool } estado atual de cada efeito
    fx_callbacks     = {}   # { cc: _FxCallback } para notificação de mudança de preset
    preset_callbacks = []   # todos os _PresetCallback registrados (para apagar LEDs)
    midi             = None

_state = _SharedState()


# ── Callback de seleção de preset ─────────────────────────────────────────────

class _PresetCallback(Callback):
    def __init__(self, pc, channel, color, text):
        super().__init__()
        self._pc      = pc
        self._channel = channel
        self._color   = color
        self._text    = text
        _state.preset_callbacks.append(self)

    def init(self, appl, listener=None):
        self._appl = appl
        _state.midi = appl.client.midi

    def push(self):
        # 1. Enviar Program Change
        _state.midi.send(_RawMessage([0xC0 | self._channel, self._pc]))

        # 2. Atualizar estado global
        _state.current_pc = self._pc

        # 3. Carregar fx states do preset e notificar botões de efeito
        preset = PRESETS.get(self._pc, {})
        fx = preset.get("fx", {})
        for cc, active in fx.items():
            _state.fx_states[cc] = active
            cb = _state.fx_callbacks.get(cc)
            if cb:
                cb.update_displays()

        # 4. Apagar LEDs de todos os outros botões de preset
        for cb in _state.preset_callbacks:
            cb.update_displays()

    def update_displays(self):
        is_active = (_state.current_pc == self._pc)
        self.action.switch_color      = self._color
        self.action.switch_brightness = 1.0 if is_active else 0.05
        if self.action.label:
            self.action.label.text       = self._text
            self.action.label.back_color = self._color


# ── Callback de toggle de efeito ──────────────────────────────────────────────

class _FxCallback(Callback):
    def __init__(self, cc, channel, color_on, color_off, text):
        super().__init__()
        self._cc        = cc
        self._channel   = channel
        self._color_on  = color_on
        self._color_off = color_off
        self._text      = text
        _state.fx_states.setdefault(cc, False)
        _state.fx_callbacks[cc] = self

    def init(self, appl, listener=None):
        self._appl = appl
        _state.midi = appl.client.midi

    def push(self):
        new_state = not _state.fx_states.get(self._cc, False)
        _state.fx_states[self._cc] = new_state
        _state.midi.send(_RawMessage([0xB0 | self._channel, self._cc, 127 if new_state else 0]))
        self.update_displays()

    def update_displays(self):
        active = _state.fx_states.get(self._cc, False)
        self.action.switch_color      = self._color_on if active else self._color_off
        self.action.switch_brightness = 1.0 if active else 0.05
        if self.action.label:
            self.action.label.text       = self._text
            self.action.label.back_color = self._color_on if active else self._color_off


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
