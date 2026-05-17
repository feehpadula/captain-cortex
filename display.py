from micropython import const
from pyswitch.colors import Colors
from pyswitch.colors import DEFAULT_LABEL_COLOR
from pyswitch.ui.ui import DisplayElement
from pyswitch.ui.ui import DisplayBounds
from pyswitch.ui.elements import DisplayLabel

_ACTION_LABEL_LAYOUT = {
    "font": "/fonts/H20.pcf",
    "backColor": DEFAULT_LABEL_COLOR,
    "stroke": 1,
    
}

_DISPLAY_WIDTH = const(
    240
)
_DISPLAY_HEIGHT = const(
    240
)
_SLOT_WIDTH = const(
    120
)
_SLOT_HEIGHT = const(
    40
)
_FOOTER_Y = const(
    200
)
_RIG_NAME_HEIGHT = const(
    160
)


DISPLAY_HEADER_1 = DisplayLabel(
    layout = {
        "font": "/fonts/A15.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }, 
    bounds = DisplayBounds(
        x = 0, 
        y = 0, 
        w = 80, 
        h = 30
    )
)

DISPLAY_HEADER_2 = DisplayLabel(
    layout = {
        "font": "/fonts/A15.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }, 
    bounds = DisplayBounds(
        x = 80, 
        y = 0, 
        w = 80, 
        h = 30
    )
)

DISPLAY_HEADER_3 = DisplayLabel(
    layout = {
        "font": "/fonts/A15.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }, 
    bounds = DisplayBounds(
        x = 160, 
        y = 0, 
        w = 80, 
        h = 30
    )
)

DISPLAY_HEADER_4 = DisplayLabel(
    layout = {
        "font": "/fonts/A15.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }, 
    bounds = DisplayBounds(
        x = 0, 
        y = 30, 
        w = 80, 
        h = 30
    )
)

DISPLAY_HEADER_5 = DisplayLabel(
    bounds = DisplayBounds(
        x = 80, 
        y = 30, 
        w = 80, 
        h = 30
    ), 
    layout = {
        "font": "/fonts/A15.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_HEADER_6 = DisplayLabel(
    bounds = DisplayBounds(
        x = 160, 
        y = 30, 
        w = 80, 
        h = 30
    ), 
    layout = {
        "font": "/fonts/A15.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_PRESET_NAME = DisplayLabel(
    bounds = DisplayBounds(
        x = 0, 
        y = 60, 
        w = 240, 
        h = 120
    ), 
    layout = {
        "font": "/fonts/PTSans-NarrowBold-40.pcf",
        "lineSpacing": 0.8,
        "maxTextWidth": 240,
    }
)

DISPLAY_PAGER = DisplayLabel(
    bounds = DisplayBounds(
        x = 0, 
        y = 180, 
        w = 240, 
        h = 60
    ), 
    layout = {
        "font": "/fonts/PTSans-NarrowBold-40.pcf",
        "backColor": Colors.WHITE,
        "stroke": 1,
        "textColor": Colors.BLACK,
        "maxTextWidth": 240,
    }
)

from pyswitch.controller.callbacks import Callback

class _StaticSplash(Callback):
    def __init__(self, root):
        Callback.__init__(self)
        self._root = root
    def get_root(self):
        return self._root

Splashes = _StaticSplash(
    DisplayElement(
        bounds = DisplayBounds(
            x = 0, 
            y = 0, 
            w = _DISPLAY_WIDTH, 
            h = _DISPLAY_HEIGHT
        ), 
        children = [
            DISPLAY_HEADER_1,
            DISPLAY_HEADER_2,
            DISPLAY_HEADER_3,
            DISPLAY_HEADER_4,
            DISPLAY_HEADER_5,
            DISPLAY_HEADER_6,
            DISPLAY_PRESET_NAME,
            DISPLAY_PAGER,
        ]
    )
)
