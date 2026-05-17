from pyswitch.clients.local.actions.custom import CUSTOM_MESSAGE
from pyswitch.clients.local.actions.rotate import ROTATING_MESSAGES
from pyswitch.clients.local.actions.pager import PagerAction
from display import DISPLAY_HEADER_1
from display import DISPLAY_HEADER_2
from display import DISPLAY_HEADER_3
from display import DISPLAY_HEADER_4
from display import DISPLAY_LABEL_5
from display import DISPLAY_LABEL_6
from display import DISPLAY_HEADER_5
from display import DISPLAY_HEADER_6
from display import DISPLAY_LABEL_1
from display import DISPLAY_LABEL_2
from display import DISPLAY_LABEL_3
from display import DISPLAY_LABEL_4
from display import DISPLAY_LABEL_7
from display import DISPLAY_LABEL_8
from display import DISPLAY_LABEL_9
from pyswitch.hardware.devices.pa_midicaptain_10 import *

_pager = PagerAction(
    pages = [
        {
            "id": 1,
            "color": (255,255,255),
            "text": 'A',
            
        },
        {
            "id": 2,
            "color": (255,255,255),
            "text": 'B',
            
        },
        {
            "id": 3,
            "color": (255,255,255),
            "text": 'C',
            
        },
        {
            "id": 4,
            "color": (255,255,255),
            "text": 'D',
            
        },
        
    ], 
    display = DISPLAY_LABEL_1, 
    led_brightness = 1, 
    led_brightness_off = 0.1, 
    led_brightness_on = 1
)

Inputs = [
    {
        "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_1,
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_2,
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_WHEEL_ENCODER,
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_WHEEL_BUTTON,
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_1,
        "actions": [
            CUSTOM_MESSAGE(
                message = [192, 0], 
                display = DISPLAY_LABEL_2, 
                text = '1', 
                id = 1, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 8], 
                text = '', 
                id = 2, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 16], 
                text = '', 
                id = 3, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 24], 
                text = '', 
                id = 4, 
                enable_callback = _pager.enable_callback
            ),
            
        ],
        "actionsHold": [
            ROTATING_MESSAGES(
                messages = [
                    [176, 34, 127],
                    [176, 34, 0],
                    
                ], 
                led_colors = [(0, 0, 0), (190, 190, 190)], 
                led_brightness = 1, 
                display = DISPLAY_HEADER_1, 
                display_colors = [(0, 0, 0), (190, 190, 190)], 
                texts = ['Gate']
            ),
            
        ],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_2,
        "actions": [
            CUSTOM_MESSAGE(
                message = [192, 1], 
                display = DISPLAY_LABEL_3, 
                text = '2', 
                id = 1, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 9], 
                text = '', 
                id = 2, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 17], 
                text = '', 
                id = 3, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 25], 
                text = '', 
                id = 4, 
                enable_callback = _pager.enable_callback
            ),
            
        ],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_3,
        "actions": [
            CUSTOM_MESSAGE(
                message = [192, 2], 
                display = DISPLAY_LABEL_4, 
                text = '3', 
                id = 1, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 10], 
                text = '', 
                id = 2, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 18], 
                text = '', 
                id = 3, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 26], 
                text = '', 
                id = 4, 
                enable_callback = _pager.enable_callback
            ),
            
        ],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_4,
        "actions": [
            CUSTOM_MESSAGE(
                message = [192, 3], 
                display = DISPLAY_LABEL_5, 
                text = '4', 
                id = 1, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 11], 
                text = '', 
                id = 2, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 19], 
                text = '', 
                id = 3, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 27], 
                text = '', 
                id = 4, 
                enable_callback = _pager.enable_callback
            ),
            
        ],
        "actionsHold": [],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_UP,
        "actions": [
            _pager.proxy(
                page_id = 1
            ),
            
        ],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_A,
        "actionsHold": [
            ROTATING_MESSAGES(
                messages = [
                    [176, 37, 127],
                    [176, 37, 0],
                    
                ], 
                led_colors = [(0, 0, 0), (190, 10, 90)], 
                led_brightness = 1, 
                display = DISPLAY_HEADER_2, 
                display_colors = [(0, 0, 0), (190, 10, 90)], 
                texts = ['Pitch']
            ),
            
        ],
        "actions": [
            CUSTOM_MESSAGE(
                message = [192, 4], 
                display = DISPLAY_LABEL_6, 
                text = 'A', 
                id = 1, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 12], 
                text = '', 
                id = 2, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 20], 
                text = '', 
                id = 3, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 28], 
                text = '', 
                id = 4, 
                enable_callback = _pager.enable_callback
            ),
            
        ],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_B,
        "actionsHold": [
            ROTATING_MESSAGES(
                messages = [
                    [176, 38, 127],
                    [176, 38, 0],
                    
                ], 
                led_colors = [(0, 0, 0), (190, 10, 90)], 
                led_brightness = 1, 
                display = DISPLAY_HEADER_3, 
                display_colors = [(0, 0, 0), (190, 10, 90)], 
                texts = ['Drive']
            ),
            
        ],
        "actions": [
            CUSTOM_MESSAGE(
                message = [192, 5], 
                display = DISPLAY_LABEL_7, 
                text = 'B', 
                id = 1, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 13], 
                text = '',
                id = 2, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 21], 
                text = '', 
                id = 3, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 29], 
                text = '', 
                id = 4, 
                enable_callback = _pager.enable_callback
            ),
            
        ],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_C,
        "actionsHold": [
            ROTATING_MESSAGES(
                messages = [
                    [176, 39, 127],
                    [176, 39, 0],
                    
                ], 
                led_colors = [(0, 0, 0), (190, 10, 90)], 
                led_brightness = 1, 
                display = DISPLAY_HEADER_4, 
                display_colors = [(0, 0, 0), (190, 10, 90)], 
                texts = ['Mod']
            ),
            
        ],
        "actions": [
            CUSTOM_MESSAGE(
                message = [192, 6], 
                display = DISPLAY_LABEL_8, 
                text = 'C', 
                id = 1, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 14], 
                text = '', 
                id = 2, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 22], 
                text = '', 
                id = 3, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 30], 
                text = '', 
                id = 4, 
                enable_callback = _pager.enable_callback
            ),
            
        ],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_D,
        "actionsHold": [
            ROTATING_MESSAGES(
                messages = [
                    [176, 40, 127],
                    [176, 40, 0],
                    
                ], 
                led_colors = [(0, 0, 0), (190, 10, 90)], 
                led_brightness = 1, 
                display = DISPLAY_HEADER_5, 
                display_colors = [(0, 0, 0), (190, 10, 90)], 
                texts = ['Delay']
            ),
            
        ],
        "actions": [
            CUSTOM_MESSAGE(
                message = [192, 7], 
                display = DISPLAY_LABEL_9, 
                text = 'D', 
                id = 1, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 15], 
                text = '', 
                id = 2, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 23], 
                text = '', 
                id = 3, 
                enable_callback = _pager.enable_callback
            ),
            CUSTOM_MESSAGE(
                message = [192, 31], 
                text = '', 
                id = 4, 
                enable_callback = _pager.enable_callback
            ),
            
        ],
        
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_DOWN,
        "actionsHold": [
            ROTATING_MESSAGES(
                messages = [
                    [176, 41, 127],
                    [176, 41, 0],
                    
                ], 
                led_colors = [(0, 0, 0), (190, 10, 90)], 
                led_brightness = 1, 
                display = DISPLAY_HEADER_6, 
                display_colors = [(0, 0, 0), (190, 10, 90)], 
                texts = ['Rev']
            ),
            
        ],
        "actions": [
            _pager,
            
        ],
        
    },
    
]
