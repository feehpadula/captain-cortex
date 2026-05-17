##############################################################################################################################################
#
# preset_manager.py — Gerenciador de presets e paginação para Nano Cortex
#
# COMO EDITAR:
#   Cada entrada em PRESETS representa um preset da Nano Cortex.
#   A chave é o número do Program Change (0-based).
#
#   Campos:
#     "name"  : Nome exibido no display central
#     "fx"    : Estado inicial de cada efeito
#                 Chave = CC number, Valor = True (ligado) / False (desligado)
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
# Implementação interna — não editar abaixo desta linha
##############################################################################################################################################

from adafruit_midi.midi_message import MIDIMessage
from display import DISPLAY_PRESET_NAME as _DISPLAY_PRESET_NAME
from display import DISPLAY_PAGER      as _DISPLAY_PAGER

PAGES        = ["A", "B", "C", "D"]
SWITCH_NAMES = ["1", "2", "3", "4", "A", "B", "C", "D"]


class _RawMessage(MIDIMessage):
    def __init__(self, data):
        self.__data = bytearray(data)
    def __bytes__(self):
        return self.__data


class _State:
    current_page    = 0
    current_pc      = -1
    active_page     = -1   # página onde o preset ativo foi selecionado
    fx_states       = {}
    preset_switches = []
    fx_switches     = {}
    fx_labels       = {}
    fx_colors       = {}
    fx_texts        = {}
    midi            = None

_st = _State()

# Inicializa o display do pager com a página A
_DISPLAY_PAGER.text = "A"


def _set_pixels(switch, color, brightness):
    """Seta todos os pixels de um switch diretamente."""
    colors = switch.colors
    for i in range(len(colors)):
        colors[i] = color
    switch.colors = colors
    bri = switch.brightnesses
    for i in range(len(bri)):
        bri[i] = brightness
    switch.brightnesses = bri


def _set_last_pixel(switch, color, brightness):
    """Seta apenas o último pixel do switch (usado pelo FX quando compartilha com preset)."""
    colors = switch.colors
    colors[-1] = color
    switch.colors = colors
    bri = switch.brightnesses
    bri[-1] = brightness
    switch.brightnesses = bri


def _set_first_pixels(switch, color, brightness):
    """Seta todos os pixels exceto o último (usado pelo preset quando compartilha com FX)."""
    n = len(switch.colors)
    colors = switch.colors
    for i in range(n - 1):
        colors[i] = color
    switch.colors = colors
    bri = switch.brightnesses
    for i in range(n - 1):
        bri[i] = brightness
    switch.brightnesses = bri


def _refresh_preset_leds():
    """Atualiza os LEDs dos 8 switches de preset conforme página e preset ativo."""
    page = _st.current_page
    for sw_idx, switch in enumerate(_st.preset_switches):
        if switch is None:
            continue
        pc = page * 8 + sw_idx
        is_active = (pc == _st.current_pc)
        has_fx = any(sw is switch for sw in _st.fx_switches.values())
        color = (0, 190, 190) if is_active else (255, 255, 255)
        bri   = 1.0 if is_active else 0.05
        if has_fx:
            _set_first_pixels(switch, color, bri)
        else:
            _set_pixels(switch, color, bri)


def _refresh_fx_leds():
    """Atualiza os LEDs dos switches de efeito."""
    for cc, switch in _st.fx_switches.items():
        active = _st.fx_states.get(cc, False)
        color_on, color_off = _st.fx_colors.get(cc, ((190, 10, 90), (0, 0, 0)))
        color = color_on if active else color_off
        bri   = 1.0 if active else 0.05
        _set_last_pixel(switch, color, bri)
        label = _st.fx_labels.get(cc)
        if label:
            label.text       = _st.fx_texts.get(cc, "")
            label.back_color = color


def _refresh_pager_display():
    """Atualiza o label do pager."""
    page_name = PAGES[_st.current_page]
    if _st.current_pc >= 0 and _st.current_page == _st.active_page:
        sw_idx  = _st.current_pc % 8
        sw_name = SWITCH_NAMES[sw_idx]
        _DISPLAY_PAGER.text = f"{page_name}{sw_name} - {_st.current_pc + 1}"
    else:
        _DISPLAY_PAGER.text = page_name


# ── Callbacks ──────────────────────────────────────────────────────────────────

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


class _PresetCallback(_BaseCallback):
    """Callback para os 8 switches de preset (1,2,3,4,A,B,C,D)."""

    def __init__(self, sw_idx, channel):
        super().__init__()
        self._sw_idx  = sw_idx
        self._channel = channel

    def init(self, appl, listener=None):
        self._appl = appl
        _st.midi   = appl.client.midi
        # Registra o switch físico
        while len(_st.preset_switches) <= self._sw_idx:
            _st.preset_switches.append(None)
        _st.preset_switches[self._sw_idx] = self.action.switch

    def push(self):
        pc = _st.current_page * 8 + self._sw_idx
        _st.current_pc = pc
        _st.active_page = _st.current_page
        _st.midi.send(_RawMessage([0xC0 | self._channel, pc]))

        preset = PRESETS.get(pc, {})
        _DISPLAY_PRESET_NAME.text = preset.get("name", "")
        for cc, active in preset.get("fx", {}).items():
            _st.fx_states[cc] = active

        _refresh_preset_leds()
        _refresh_fx_leds()
        _refresh_pager_display()

    def update_displays(self):
        sw_idx = self._sw_idx
        pc     = _st.current_page * 8 + sw_idx
        switch = self.action.switch
        if switch:
            is_active = (pc == _st.current_pc)
            has_fx = any(sw is switch for sw in _st.fx_switches.values())
            color = (0, 190, 190) if is_active else (255, 255, 255)
            bri   = 1.0 if is_active else 0.05
            if has_fx:
                _set_first_pixels(switch, color, bri)
            else:
                _set_pixels(switch, color, bri)


class _PageCallback(_BaseCallback):
    """Callback para o Switch DOWN — troca de página."""

    def __init__(self):
        super().__init__()

    def push(self):
        _st.current_page = (_st.current_page + 1) % len(PAGES)
        _refresh_preset_leds()
        _refresh_pager_display()


class _PageDirectCallback(_BaseCallback):
    """Callback para o Switch UP — recua uma página."""

    def push(self):
        _st.current_page = (_st.current_page - 1) % len(PAGES)
        _refresh_preset_leds()
        _refresh_pager_display()


class _FxCallback(_BaseCallback):
    """Callback para os switches de efeito (actionsHold)."""

    def __init__(self, cc, channel, color_on, color_off, text):
        super().__init__()
        self._cc        = cc
        self._channel   = channel
        self._color_on  = color_on
        self._color_off = color_off
        self._text      = text
        _st.fx_states.setdefault(cc, False)
        _st.fx_colors[cc] = (color_on, color_off)
        _st.fx_texts[cc]  = text

    def init(self, appl, listener=None):
        self._appl = appl
        _st.midi   = appl.client.midi
        _st.fx_switches[self._cc] = self.action.switch
        if self.action.label:
            _st.fx_labels[self._cc] = self.action.label

    def push(self):
        new_state = not _st.fx_states.get(self._cc, False)
        _st.fx_states[self._cc] = new_state
        _st.midi.send(_RawMessage([0xB0 | self._channel, self._cc, 127 if new_state else 0]))
        _refresh_fx_leds()

    def update_displays(self):
        active = _st.fx_states.get(self._cc, False)
        color  = self._color_on if active else self._color_off
        switch = self.action.switch
        if switch:
            _set_last_pixel(switch, color, 1.0 if active else 0.05)
        if self.action.label:
            self.action.label.text       = self._text
            self.action.label.back_color = color


# ── Fábricas de Action ─────────────────────────────────────────────────────────

from pyswitch.controller.actions import Action


def PRESET_SWITCH(sw_idx, channel=0):
    """
    Cria a action para um dos 8 switches de preset.
    sw_idx: 0=Switch1, 1=Switch2, 2=Switch3, 3=Switch4,
            4=SwitchA, 5=SwitchB, 6=SwitchC, 7=SwitchD
    """
    return Action({
        "callback":      _PresetCallback(sw_idx=sw_idx, channel=channel),
        "useSwitchLeds": False,  # LEDs controlados diretamente por _set_pixels
    })


def PAGE_NEXT():
    """Action para o Switch DOWN — avança página."""
    return Action({
        "callback":      _PageCallback(),
        "useSwitchLeds": False,
    })


def PAGE_FIRST():
    """Action para o Switch UP — volta para página A."""
    return Action({
        "callback":      _PageDirectCallback(),
        "useSwitchLeds": False,
    })


def EFFECT_TOGGLE(cc, channel=0, color_on=(190, 10, 90), color_off=(0, 0, 0), display=None, text=""):
    """Action para toggle de efeito (actionsHold)."""
    return Action({
        "callback":      _FxCallback(cc=cc, channel=channel, color_on=color_on, color_off=color_off, text=text),
        "display":       display,
        "useSwitchLeds": False,
    })
