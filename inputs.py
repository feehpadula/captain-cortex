from pyswitch.clients.local.actions.pager import PagerAction
from pyswitch.hardware.devices.pa_midicaptain_10 import *

from preset_manager import PRESET_SELECT, EFFECT_TOGGLE

from display import DISPLAY_HEADER_1
from display import DISPLAY_HEADER_2
from display import DISPLAY_HEADER_3
from display import DISPLAY_HEADER_4
from display import DISPLAY_HEADER_5
from display import DISPLAY_HEADER_6
from display import DISPLAY_LABEL_1

# ── MIDI channel (0 = canal 1) ─────────────────────────────────────────────────
_CH = 0

# ── Cores dos botões de efeito ─────────────────────────────────────────────────
_OFF  = (0,   0,   0)
_FX   = (190, 10,  90)

# ── Pager (troca de página A/B/C/D) ───────────────────────────────────────────
_pager = PagerAction(
    pages = [
        { "id": 1, "color": (255, 255, 255), "text": "A" },
        { "id": 2, "color": (255, 255, 255), "text": "B" },
        { "id": 3, "color": (255, 255, 255), "text": "C" },
        { "id": 4, "color": (255, 255, 255), "text": "D" },
    ],
    display            = DISPLAY_LABEL_1,
    led_brightness     = 1,
    led_brightness_off = 0.1,
    led_brightness_on  = 1,
)

Inputs = [
    { "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_1    },
    { "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_2    },
    { "assignment": PA_MIDICAPTAIN_10_WHEEL_ENCODER   },
    { "assignment": PA_MIDICAPTAIN_10_WHEEL_BUTTON    },

    # ── Switch 1 — presets 1 / 9 / 17 / 25  ──────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_1,
        "actions": [
            PRESET_SELECT(pc=0,  channel=_CH, text="", id=1, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=8,  channel=_CH, text="", id=2, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=16, channel=_CH, text="", id=3, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=24, channel=_CH, text="", id=4, enable_callback=_pager.enable_callback),
        ],
        "actionsHold": [
            EFFECT_TOGGLE(cc=34, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_1, text="GATE"),
        ],
    },

    # ── Switch 2 — presets 2 / 10 / 18 / 26 ──────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_2,
        "actions": [
            PRESET_SELECT(pc=1,  channel=_CH, text="", id=1, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=9,  channel=_CH, text="", id=2, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=17, channel=_CH, text="", id=3, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=25, channel=_CH, text="", id=4, enable_callback=_pager.enable_callback),
        ],
    },

    # ── Switch 3 — presets 3 / 11 / 19 / 27 ──────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_3,
        "actions": [
            PRESET_SELECT(pc=2,  channel=_CH, text="", id=1, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=10, channel=_CH, text="", id=2, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=18, channel=_CH, text="", id=3, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=26, channel=_CH, text="", id=4, enable_callback=_pager.enable_callback),
        ],
    },

    # ── Switch 4 — presets 4 / 12 / 20 / 28 ──────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_4,
        "actions": [
            PRESET_SELECT(pc=3,  channel=_CH, text="", id=1, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=11, channel=_CH, text="", id=2, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=19, channel=_CH, text="", id=3, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=27, channel=_CH, text="", id=4, enable_callback=_pager.enable_callback),
        ],
        "actionsHold": [],
    },

    # ── Switch UP — avança para página A ──────────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_UP,
        "actions": [
            _pager.proxy(page_id=1),
        ],
    },

    # ── Switch A — presets 5 / 13 / 21 / 29 ──────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_A,
        "actions": [
            PRESET_SELECT(pc=4,  channel=_CH, text="", id=1, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=12, channel=_CH, text="", id=2, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=20, channel=_CH, text="", id=3, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=28, channel=_CH, text="", id=4, enable_callback=_pager.enable_callback),
        ],
        "actionsHold": [
            EFFECT_TOGGLE(cc=37, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_2, text="FX 1"),
        ],
    },

    # ── Switch B — presets 6 / 14 / 22 / 30 ──────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_B,
        "actions": [
            PRESET_SELECT(pc=5,  channel=_CH, text="", id=1, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=13, channel=_CH, text="", id=2, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=21, channel=_CH, text="", id=3, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=29, channel=_CH, text="", id=4, enable_callback=_pager.enable_callback),
        ],
        "actionsHold": [
            EFFECT_TOGGLE(cc=38, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_3, text="FX 2"),
        ],
    },

    # ── Switch C — presets 7 / 15 / 23 / 31 ──────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_C,
        "actions": [
            PRESET_SELECT(pc=6,  channel=_CH, text="", id=1, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=14, channel=_CH, text="", id=2, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=22, channel=_CH, text="", id=3, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=30, channel=_CH, text="", id=4, enable_callback=_pager.enable_callback),
        ],
        "actionsHold": [
            EFFECT_TOGGLE(cc=39, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_4, text="FX 3"),
        ],
    },

    # ── Switch D — presets 8 / 16 / 24 / 32 ──────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_D,
        "actions": [
            PRESET_SELECT(pc=7,  channel=_CH, text="", id=1, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=15, channel=_CH, text="", id=2, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=23, channel=_CH, text="", id=3, enable_callback=_pager.enable_callback),
            PRESET_SELECT(pc=31, channel=_CH, text="", id=4, enable_callback=_pager.enable_callback),
        ],
        "actionsHold": [
            EFFECT_TOGGLE(cc=40, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_5, text="FX 4"),
        ],
    },

    # ── Switch DOWN — troca de página  +  hold: FX 5 ──────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_DOWN,
        "actions": [
            _pager,
        ],
        "actionsHold": [
            EFFECT_TOGGLE(cc=41, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_6, text="FX 5"),
        ],
    },
]
