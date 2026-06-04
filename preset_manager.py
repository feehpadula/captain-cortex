##############################################################################################################################################
#
# preset_manager.py — Gerenciador de presets e paginação para Nano Cortex
#
# Os presets são definidos em presets.py — edite aquele arquivo.
#
##############################################################################################################################################

from presets import PRESETS

##############################################################################################################################################
# Implementação interna — não editar abaixo desta linha
##############################################################################################################################################

from pyswitch.misc import get_current_millis
from pyswitch.controller.actions import Action
from adafruit_midi.midi_message import MIDIMessage
from display import DISPLAY_PRESET_NAME as _DISPLAY_PRESET_NAME
from display import DISPLAY_PAGER      as _DISPLAY_PAGER

PAGES        = ["A", "B", "C", "D"]
SWITCH_NAMES = ["1", "2", "3", "4", "A", "B", "C", "D"]

_COLOR_PRESET_ACTIVE = (0,   190, 190)   # ciano
_COLOR_PRESET_DIM    = (255, 255, 255)   # branco dim
_COLOR_TAP           = (190, 10,  90)    # rosa
_COLOR_OFF           = (0,   0,   0)


class _RawMessage(MIDIMessage):
    def __init__(self, data):
        self.__data = bytearray(data)
    def __bytes__(self):
        return self.__data


# ── Estado global ──────────────────────────────────────────────────────────────

class _State:
    current_page    = 0
    current_pc      = -1
    active_page     = -1
    fx_states       = {}
    preset_switches = []
    fx_switches     = {}
    fx_labels       = {}
    fx_colors       = {}
    fx_texts        = {}
    midi            = None
    appl            = None

    # Tap tempo
    tap_mode        = False
    tap_bpm         = 0        # BPM atual (0 = sem tap ainda)
    tap_last_ms     = 0        # timestamp do último tap
    tap_interval_ms = 0        # intervalo calculado entre taps
    tap_led_on      = False    # estado atual do LED do DOWN piscando
    tap_last_blink  = 0        # timestamp do último blink

    # Referências aos switches do UP e DOWN
    switch_up       = None
    switch_down     = None

_st = _State()

_DISPLAY_PAGER.text = "A"


# ── Helpers de LED ─────────────────────────────────────────────────────────────

def _set_pixels(switch, color, brightness):
    colors = switch.colors
    for i in range(len(colors)):
        colors[i] = color
    switch.colors = colors
    bri = switch.brightnesses
    for i in range(len(bri)):
        bri[i] = brightness
    switch.brightnesses = bri


def _set_last_pixel(switch, color, brightness):
    colors = switch.colors
    colors[-1] = color
    switch.colors = colors
    bri = switch.brightnesses
    bri[-1] = brightness
    switch.brightnesses = bri


def _set_first_pixels(switch, color, brightness):
    n = len(switch.colors)
    colors = switch.colors
    for i in range(n - 1):
        colors[i] = color
    switch.colors = colors
    bri = switch.brightnesses
    for i in range(n - 1):
        bri[i] = brightness
    switch.brightnesses = bri


# ── Refresh ────────────────────────────────────────────────────────────────────

def _refresh_preset_leds():
    page = _st.current_page
    for sw_idx, switch in enumerate(_st.preset_switches):
        if switch is None:
            continue
        pc = page * 8 + sw_idx
        is_active = (pc == _st.current_pc)
        has_fx = any(sw is switch for sw in _st.fx_switches.values())
        color = _COLOR_PRESET_ACTIVE if is_active else _COLOR_PRESET_DIM
        bri   = 1.0 if is_active else 0.05
        if has_fx:
            _set_first_pixels(switch, color, bri)
        else:
            _set_pixels(switch, color, bri)


def _refresh_fx_leds():
    for cc, switch in _st.fx_switches.items():
        active = _st.fx_states.get(cc, False)
        color_on, color_off = _st.fx_colors.get(cc, (_COLOR_TAP, _COLOR_OFF))
        color = color_on if active else color_off
        bri   = 1.0 if active else 0.05
        _set_last_pixel(switch, color, bri)
        label = _st.fx_labels.get(cc)
        if label:
            label.text       = _st.fx_texts.get(cc, "")
            label.back_color = color


def _refresh_pager_display():
    page_name = PAGES[_st.current_page]
    if _st.current_pc >= 0 and _st.current_page == _st.active_page:
        sw_idx  = _st.current_pc % 8
        sw_name = SWITCH_NAMES[sw_idx]
        _DISPLAY_PAGER.text = f"{page_name}{sw_name} - {_st.current_pc + 1}"
    else:
        _DISPLAY_PAGER.text = page_name


# ── Tap Tempo ──────────────────────────────────────────────────────────────────

def _bpm_to_ms(bpm):
    return int(60000 / bpm) if bpm > 0 else 500


def _enter_tap_mode():
    _st.tap_mode    = True
    _st.tap_bpm     = 0
    _st.tap_last_ms = 0
    _st.tap_led_on  = False
    _st.tap_last_blink = get_current_millis()

    # Apaga todos os LEDs de preset e FX
    for switch in _st.preset_switches:
        if switch:
            _set_pixels(switch, _COLOR_OFF, 0)
    for switch in _st.fx_switches.values():
        _set_pixels(switch, _COLOR_OFF, 0)

    # UP: apenas o pixel [2] fica rosa, os outros apagados
    if _st.switch_up:
        colors = _st.switch_up.colors
        for i in range(len(colors)):
            colors[i] = _COLOR_TAP if i == 2 else _COLOR_OFF
        _st.switch_up.colors = colors
        bri = _st.switch_up.brightnesses
        for i in range(len(bri)):
            bri[i] = 1.0 if i == 2 else 0
        _st.switch_up.brightnesses = bri

    # DOWN começa apagado — vai piscar em ciano no update
    if _st.switch_down:
        _set_pixels(_st.switch_down, _COLOR_OFF, 0)

    # Display mostra "TAP" enquanto não há BPM
    _DISPLAY_PRESET_NAME.text = "TAP"
    _DISPLAY_PAGER.text = ""


def _exit_tap_mode():
    _st.tap_mode = False
    _refresh_preset_leds()
    _refresh_fx_leds()
    _refresh_pager_display()
    if _st.current_pc >= 0:
        preset = PRESETS.get(_st.current_pc, {})
        _DISPLAY_PRESET_NAME.text = preset.get("name", "")
    else:
        _DISPLAY_PRESET_NAME.text = ""
    # Apaga UP e DOWN completamente
    if _st.switch_up:
        _set_pixels(_st.switch_up, _COLOR_PRESET_DIM, 0.05)
    if _st.switch_down:
        _set_pixels(_st.switch_down, _COLOR_PRESET_DIM, 0.05)
    # Reaplica FX leds por cima (corrige switches que têm FX no hold)
    _refresh_fx_leds()


def _tap():
    """Registra um tap e calcula o BPM."""
    now = get_current_millis()
    if _st.tap_last_ms > 0:
        interval = now - _st.tap_last_ms
        # Ignora intervalos absurdos (> 3s = novo tap do zero)
        if interval < 3000:
            _st.tap_interval_ms = interval
            bpm = int(60000 / interval)
            _st.tap_bpm = bpm
            _DISPLAY_PRESET_NAME.text = f"{bpm} BPM"
            # Envia CC#42 para a Nano Cortex
            _st.midi.send(_RawMessage([0xB0, 42, 64]))
    _st.tap_last_ms = now
    # Sincroniza o blink com o tap
    _st.tap_led_on     = True
    _st.tap_last_blink = now
    if _st.switch_down:
        _set_pixels(_st.switch_down, _COLOR_PRESET_ACTIVE, 1.0)


def _update_tap_blink():
    if not _st.tap_mode or not _st.switch_down:
        return
    interval = _st.tap_interval_ms if _st.tap_interval_ms > 0 else 500
    half     = interval // 2
    now      = get_current_millis()
    if now - _st.tap_last_blink >= half:
        _st.tap_last_blink = now
        _st.tap_led_on = not _st.tap_led_on
        bri = 1.0 if _st.tap_led_on else 0.02
        _set_pixels(_st.switch_down, _COLOR_PRESET_ACTIVE, bri)


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
    def __init__(self, sw_idx, channel):
        super().__init__()
        self._sw_idx  = sw_idx
        self._channel = channel

    def init(self, appl, listener=None):
        self._appl = appl
        _st.midi = appl.client.midi
        _st.appl = appl
        while len(_st.preset_switches) <= self._sw_idx:
            _st.preset_switches.append(None)
        _st.preset_switches[self._sw_idx] = self.action.switch

    def push(self):
        if _st.tap_mode:
            return  # ignora presets em modo tap
        pc = _st.current_page * 8 + self._sw_idx
        _st.current_pc  = pc
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
        if _st.tap_mode:
            return
        sw_idx = self._sw_idx
        pc     = _st.current_page * 8 + sw_idx
        switch = self.action.switch
        if switch:
            is_active = (pc == _st.current_pc)
            has_fx    = any(sw is switch for sw in _st.fx_switches.values())
            color = _COLOR_PRESET_ACTIVE if is_active else _COLOR_PRESET_DIM
            bri   = 1.0 if is_active else 0.05
            if has_fx:
                _set_first_pixels(switch, color, bri)
            else:
                _set_pixels(switch, color, bri)


class _PageCallback(_BaseCallback):
    """Switch DOWN — avança página / tap tempo em modo tap."""

    def init(self, appl, listener=None):
        self._appl = appl
        _st.midi = appl.client.midi
        _st.switch_down = self.action.switch

    def push(self):
        if _st.tap_mode:
            _tap()
            return
        _st.current_page = (_st.current_page + 1) % len(PAGES)
        _refresh_preset_leds()
        _refresh_pager_display()

    def update(self):
        # Chamado periodicamente — atualiza o blink do tap
        _update_tap_blink()

    def update_displays(self):
        if _st.tap_mode:
            return
        if _st.switch_down:
            _set_pixels(_st.switch_down, _COLOR_PRESET_DIM, 0.05)


class _PageUpCallback(_BaseCallback):
    """Switch UP — recua página / entra e sai do modo tap (hold)."""

    def init(self, appl, listener=None):
        self._appl = appl
        _st.switch_up = self.action.switch

    def push(self):
        if _st.tap_mode:
            _exit_tap_mode()
            return
        _st.current_page = (_st.current_page - 1) % len(PAGES)
        _refresh_preset_leds()
        _refresh_pager_display()

    def update_displays(self):
        if _st.tap_mode:
            return
        if _st.switch_up:
            _set_pixels(_st.switch_up, _COLOR_PRESET_DIM, 0.05)


class _TapModeCallback(_BaseCallback):
    """Hold no UP — entra no modo tap tempo."""

    def push(self):
        if not _st.tap_mode:
            _enter_tap_mode()


class _FxCallback(_BaseCallback):
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
        _st.midi = appl.client.midi
        _st.fx_switches[self._cc] = self.action.switch
        if self.action.label:
            _st.fx_labels[self._cc] = self.action.label

    def push(self):
        if _st.tap_mode:
            return
        new_state = not _st.fx_states.get(self._cc, False)
        _st.fx_states[self._cc] = new_state
        _st.midi.send(_RawMessage([0xB0 | self._channel, self._cc, 127 if new_state else 0]))
        _refresh_fx_leds()

    def update_displays(self):
        if _st.tap_mode:
            return
        active = _st.fx_states.get(self._cc, False)
        color  = self._color_on if active else self._color_off
        switch = self.action.switch
        if switch:
            _set_last_pixel(switch, color, 1.0 if active else 0.05)
        if self.action.label:
            self.action.label.text       = self._text
            self.action.label.back_color = color


# ── Fábricas de Action ─────────────────────────────────────────────────────────

from pyswitch.misc import Updateable as _Updateable


class _UpdatableAction(Action, _Updateable):
    """Action que também participa do loop de update do controller."""
    def __init__(self, config):
        Action.__init__(self, config)

    def update(self):
        if self.callback and hasattr(self.callback, "update"):
            self.callback.update()


def PRESET_SWITCH(sw_idx, channel=0):
    return Action({
        "callback":      _PresetCallback(sw_idx=sw_idx, channel=channel),
        "useSwitchLeds": False,
    })


def PAGE_NEXT():
    """Switch DOWN — avança página / tap no modo tap."""
    return _UpdatableAction({
        "callback":      _PageCallback(),
        "useSwitchLeds": False,
    })


def PAGE_UP():
    """Switch UP — recua página / sai do modo tap. Hold = entra no modo tap."""
    return Action({
        "callback":      _PageUpCallback(),
        "useSwitchLeds": False,
    })


def TAP_MODE_ENTER():
    """Hold no Switch UP — entra no modo tap tempo."""
    return Action({
        "callback":      _TapModeCallback(),
        "useSwitchLeds": False,
    })


def EFFECT_TOGGLE(cc, channel=0, color_on=(190, 10, 90), color_off=(0, 0, 0), display=None, text=""):
    return Action({
        "callback":      _FxCallback(cc=cc, channel=channel, color_on=color_on, color_off=color_off, text=text),
        "display":       display,
        "useSwitchLeds": False,
    })
