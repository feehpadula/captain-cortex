##############################################################################################################################################
#
# presets.py — Definição dos presets da Nano Cortex
#
# Edite este arquivo para configurar seus presets.
#
# Cada preset ocupa duas linhas:
#   Linha 1: número do PC e nome do preset
#   Linha 2: estado dos efeitos (gate, fx1, fx2, fx3, fx4, fx5)
#
# CCs da Nano Cortex:
#   CC#34 = INPUT GATE | CC#37 = FX 1 | CC#38 = FX 2 | CC#39 = FX 3
#   CC#40 = FX 4       | CC#41 = FX 5
#
# Valores CC: 0-63 = Off, 64-127 = On
#
##############################################################################################################################################

#            gate    fx1     fx2     fx3     fx4     fx5
_ON  = True
_OFF = False

_PRESETS_RAW = [

    # ── Page A ────────────────────────────────────────────────────────────────

    (  0, "Preset 1",
         _OFF,  _OFF,  _OFF,  _OFF,  _OFF,  _OFF  ),

    (  1, "Preset 2",
         _OFF,  _ON,   _OFF,  _OFF,  _OFF,  _OFF  ),

    (  2, "Preset 3",
         _OFF,  _ON,   _ON,   _OFF,  _OFF,  _OFF  ),

    (  3, "Preset 4",
         _OFF,  _OFF,  _OFF,  _ON,   _ON,   _OFF  ),

    (  4, "Preset 5",
         _OFF,  _OFF,  _OFF,  _OFF,  _ON,   _ON   ),

    (  5, "Preset 6",
         _ON,   _OFF,  _OFF,  _OFF,  _OFF,  _OFF  ),

    (  6, "Preset 7",
         _OFF,  _ON,   _OFF,  _ON,   _OFF,  _OFF  ),

    (  7, "Preset 8",
         _OFF,  _OFF,  _ON,   _OFF,  _ON,   _OFF  ),

    # ── Page B ────────────────────────────────────────────────────────────────

    (  8, "Preset 9",
         _OFF,  _OFF,  _OFF,  _OFF,  _OFF,  _OFF  ),

    (  9, "Preset 10",
         _OFF,  _ON,   _OFF,  _OFF,  _OFF,  _OFF  ),

    ( 10, "Preset 11",
         _OFF,  _OFF,  _ON,   _OFF,  _OFF,  _OFF  ),

    ( 11, "Preset 12",
         _OFF,  _OFF,  _OFF,  _ON,   _OFF,  _OFF  ),

    ( 12, "Preset 13",
         _OFF,  _OFF,  _OFF,  _OFF,  _ON,   _OFF  ),

    ( 13, "Preset 14",
         _OFF,  _OFF,  _OFF,  _OFF,  _OFF,  _ON   ),

    ( 14, "Preset 15",
         _ON,   _ON,   _OFF,  _OFF,  _OFF,  _OFF  ),

    ( 15, "Preset 16",
         _OFF,  _ON,   _ON,   _ON,   _OFF,  _OFF  ),

    # ── Page C ────────────────────────────────────────────────────────────────

    ( 16, "Preset 17",
         _OFF,  _OFF,  _OFF,  _OFF,  _OFF,  _OFF  ),

    ( 17, "Preset 18",
         _OFF,  _ON,   _OFF,  _OFF,  _OFF,  _OFF  ),

    ( 18, "Preset 19",
         _OFF,  _OFF,  _ON,   _OFF,  _OFF,  _OFF  ),

    ( 19, "Preset 20",
         _OFF,  _OFF,  _OFF,  _ON,   _OFF,  _OFF  ),

    ( 20, "Preset 21",
         _OFF,  _OFF,  _OFF,  _OFF,  _ON,   _OFF  ),

    ( 21, "Preset 22",
         _OFF,  _OFF,  _OFF,  _OFF,  _OFF,  _ON   ),

    ( 22, "Preset 23",
         _ON,   _ON,   _ON,   _OFF,  _OFF,  _OFF  ),

    ( 23, "Preset 24",
         _OFF,  _ON,   _ON,   _ON,   _ON,   _OFF  ),

    # ── Page D ────────────────────────────────────────────────────────────────

    ( 24, "Preset 25",
         _OFF,  _OFF,  _OFF,  _OFF,  _OFF,  _OFF  ),

    ( 25, "Preset 26",
         _OFF,  _ON,   _OFF,  _OFF,  _OFF,  _OFF  ),

    ( 26, "Preset 27",
         _OFF,  _OFF,  _ON,   _OFF,  _OFF,  _OFF  ),

    ( 27, "Preset 28",
         _OFF,  _OFF,  _OFF,  _ON,   _OFF,  _OFF  ),

    ( 28, "Preset 29",
         _OFF,  _OFF,  _OFF,  _OFF,  _ON,   _OFF  ),

    ( 29, "Preset 30",
         _OFF,  _OFF,  _OFF,  _OFF,  _OFF,  _ON   ),

    ( 30, "Preset 31",
         _ON,   _OFF,  _ON,   _OFF,  _ON,   _OFF  ),

    ( 31, "Preset 32",
         _ON,   _ON,   _ON,   _ON,   _ON,   _ON   ),
]

# Converte para o formato esperado pelo preset_manager
PRESETS = {
    pc: {
        "name": name,
        "fx": {
            34: gate,
            37: fx1,
            38: fx2,
            39: fx3,
            40: fx4,
            41: fx5,
        }
    }
    for pc, name, gate, fx1, fx2, fx3, fx4, fx5 in _PRESETS_RAW
}