from pyswitch.hardware.devices.pa_midicaptain_10 import *
from preset_manager import PRESET_SWITCH, PAGE_NEXT, PAGE_UP, TAP_MODE_ENTER, EFFECT_TOGGLE

from display import DISPLAY_HEADER_1
from display import DISPLAY_HEADER_2
from display import DISPLAY_HEADER_3
from display import DISPLAY_HEADER_4
from display import DISPLAY_HEADER_5
from display import DISPLAY_HEADER_6

_CH  = 0
_OFF = (0,   0,   0)
_FX  = (190, 10,  90)

Inputs = [
    { "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_1  },
    { "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_2  },
    { "assignment": PA_MIDICAPTAIN_10_WHEEL_ENCODER },
    { "assignment": PA_MIDICAPTAIN_10_WHEEL_BUTTON  },

    # ── Switch 1 — preset slot 0  +  hold: GATE ───────────────────────────────
    {
        "assignment":  PA_MIDICAPTAIN_10_SWITCH_1,
        "actions":     [ PRESET_SWITCH(sw_idx=0, channel=_CH) ],
        "actionsHold": [ EFFECT_TOGGLE(cc=34, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_1, text="GATE") ],
    },

    # ── Switch 2 — preset slot 1 ───────────────────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_2,
        "actions":    [ PRESET_SWITCH(sw_idx=1, channel=_CH) ],
    },

    # ── Switch 3 — preset slot 2 ───────────────────────────────────────────────
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_3,
        "actions":    [ PRESET_SWITCH(sw_idx=2, channel=_CH) ],
    },

    # ── Switch 4 — preset slot 3 ───────────────────────────────────────────────
    {
        "assignment":  PA_MIDICAPTAIN_10_SWITCH_4,
        "actions":     [ PRESET_SWITCH(sw_idx=3, channel=_CH) ],
        "actionsHold": [],
    },

    # ── Switch UP — recua página  +  hold: entra no modo tap tempo ─────────────
    {
        "assignment":  PA_MIDICAPTAIN_10_SWITCH_UP,
        "actions":     [ PAGE_UP() ],
        "actionsHold": [ TAP_MODE_ENTER() ],
    },

    # ── Switch A — preset slot 4  +  hold: FX 1 ───────────────────────────────
    {
        "assignment":  PA_MIDICAPTAIN_10_SWITCH_A,
        "actions":     [ PRESET_SWITCH(sw_idx=4, channel=_CH) ],
        "actionsHold": [ EFFECT_TOGGLE(cc=37, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_2, text="FX 1") ],
    },

    # ── Switch B — preset slot 5  +  hold: FX 2 ───────────────────────────────
    {
        "assignment":  PA_MIDICAPTAIN_10_SWITCH_B,
        "actions":     [ PRESET_SWITCH(sw_idx=5, channel=_CH) ],
        "actionsHold": [ EFFECT_TOGGLE(cc=38, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_3, text="FX 2") ],
    },

    # ── Switch C — preset slot 6  +  hold: FX 3 ───────────────────────────────
    {
        "assignment":  PA_MIDICAPTAIN_10_SWITCH_C,
        "actions":     [ PRESET_SWITCH(sw_idx=6, channel=_CH) ],
        "actionsHold": [ EFFECT_TOGGLE(cc=39, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_4, text="FX 3") ],
    },

    # ── Switch D — preset slot 7  +  hold: FX 4 ───────────────────────────────
    {
        "assignment":  PA_MIDICAPTAIN_10_SWITCH_D,
        "actions":     [ PRESET_SWITCH(sw_idx=7, channel=_CH) ],
        "actionsHold": [ EFFECT_TOGGLE(cc=40, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_5, text="FX 4") ],
    },

    # ── Switch DOWN — avança página / tap tempo  +  hold: FX 5 ────────────────
    {
        "assignment":  PA_MIDICAPTAIN_10_SWITCH_DOWN,
        "actions":     [ PAGE_NEXT() ],
        "actionsHold": [ EFFECT_TOGGLE(cc=41, channel=_CH, color_on=_FX, color_off=_OFF, display=DISPLAY_HEADER_6, text="FX 5") ],
    },
]
