from pyswitch.clients.kemper import KemperRigNameCallback
from pyswitch.clients.kemper import TunerDisplayCallback
from micropython import const
from pyswitch.colors import Colors
from pyswitch.colors import DEFAULT_LABEL_COLOR
from pyswitch.ui.ui import DisplayElement
from pyswitch.ui.ui import DisplayBounds
from pyswitch.ui.elements import DisplayLabel
from pyswitch.ui.elements import BidirectionalProtocolState

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
        h = 20
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
        h = 20
    )
)


DISPLAY_FOOTER_1 = DisplayLabel(
    layout = _ACTION_LABEL_LAYOUT, 
    bounds = DisplayBounds(
        x = 0, 
        y = _FOOTER_Y, 
        w = _SLOT_WIDTH, 
        h = _SLOT_HEIGHT
    )
)
DISPLAY_FOOTER_2 = DisplayLabel(
    layout = _ACTION_LABEL_LAYOUT, 
    bounds = DisplayBounds(
        x = _SLOT_WIDTH, 
        y = _FOOTER_Y, 
        w = _SLOT_WIDTH, 
        h = _SLOT_HEIGHT
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
        h = 20
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
        y = 20, 
        w = 80, 
        h = 20
    )
)

DISPLAY_LABEL_5 = DisplayLabel(
    bounds = DisplayBounds(
        x = 200, 
        y = 160, 
        w = 40, 
        h = 40
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_LABEL_6 = DisplayLabel(
    bounds = DisplayBounds(
        x = 80, 
        y = 200, 
        w = 40, 
        h = 40
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_HEADER_5 = DisplayLabel(
    bounds = DisplayBounds(
        x = 80, 
        y = 20, 
        w = 80, 
        h = 20
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
        y = 20, 
        w = 80, 
        h = 20
    ), 
    layout = {
        "font": "/fonts/A15.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_LABEL_1 = DisplayLabel(
    bounds = DisplayBounds(
        x = 0, 
        y = 160, 
        w = 80, 
        h = 80
    ), 
    layout = {
        "font": "/fonts/PTSans-NarrowBold-40.pcf",
        "backColor": Colors.BLACK,
        "stroke": 1,
        "textColor": Colors.BLACK,
        "maxTextWidth": 160,
        
    }
)

DISPLAY_LABEL_2 = DisplayLabel(
    bounds = DisplayBounds(
        x = 80, 
        y = 160, 
        w = 40, 
        h = 40
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_LABEL_3 = DisplayLabel(
    bounds = DisplayBounds(
        x = 120, 
        y = 160, 
        w = 40, 
        h = 40
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_LABEL_4 = DisplayLabel(
    bounds = DisplayBounds(
        x = 160, 
        y = 160, 
        w = 40, 
        h = 40
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_LABEL_7 = DisplayLabel(
    bounds = DisplayBounds(
        x = 120, 
        y = 200, 
        w = 40, 
        h = 40
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_LABEL_8 = DisplayLabel(
    bounds = DisplayBounds(
        x = 160, 
        y = 200, 
        w = 40, 
        h = 40
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_LABEL_9 = DisplayLabel(
    bounds = DisplayBounds(
        x = 200, 
        y = 200, 
        w = 40, 
        h = 40
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)

DISPLAY_LABEL_10 = DisplayLabel(
    bounds = DisplayBounds(
        x = 0, 
        y = 110, 
        w = 220, 
        h = 50
    ), 
    layout = {
        "font": "/fonts/H20.pcf",
        "backColor": DEFAULT_LABEL_COLOR,
        "stroke": 1,
        
    }
)


Splashes = TunerDisplayCallback(
    splash_default = DisplayElement(
        bounds = DisplayBounds(
            x = 0, 
            y = 0, 
            w = _DISPLAY_WIDTH, 
            h = _DISPLAY_HEIGHT
        ), 
        children = [
            BidirectionalProtocolState(
                DisplayBounds(
                    x = 232, 
                    y = 40, 
                    w = 8, 
                    h = 8
                )
            ),
            DISPLAY_HEADER_1,
            DISPLAY_HEADER_2,
            DISPLAY_HEADER_3,
            DISPLAY_HEADER_4,
            DISPLAY_HEADER_5,
            DISPLAY_HEADER_6,
            DISPLAY_LABEL_1,
            DISPLAY_LABEL_2,
            DisplayLabel(
                bounds = DisplayBounds(
                    x = 0, 
                    y = 40, 
                    w = 240, 
                    h = 120
                ), 
                layout = {
                    "font": "/fonts/PTSans-NarrowBold-40.pcf",
                    "lineSpacing": 0.8,
                    "maxTextWidth": 220,
                    
                }, 
                callback = KemperRigNameCallback()
            ),
            DISPLAY_LABEL_3,
            DISPLAY_LABEL_4,
            DISPLAY_LABEL_5,
            DISPLAY_LABEL_6,
            DISPLAY_LABEL_7,
            DISPLAY_LABEL_8,
            DISPLAY_LABEL_9,
            
        ]
    )
)
