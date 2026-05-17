##############################################################################################################################################
# 
# Firmware processing configuration. Most options are optional.
#
##############################################################################################################################################

Config = {
    
    # Enables file transfer via MIDI from and to the device using PyMidiBridge.
    # DESATIVADO temporariamente para debug — reativar depois.
    # "enableMidiBridge": True,

    ## Development Options ###################################################################################################################

    # Debug output is printed to serial console via USB. 
    # See https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux 

    "debugStats": True,
    "debugStatsInterval": 2000,
    "debugSentMessages": True,
    "debugUnparsedMessages": True,
    "excludeMessageTypes": ["SystemExclusive"],
}
