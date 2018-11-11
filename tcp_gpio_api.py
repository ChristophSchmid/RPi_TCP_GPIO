"""
'Mini'-API for a TCP-based communication of a Raspberry Pi
with another device in a LAN. Can be extended as needed.
"""

import RPi.GPIO as GPIO

# list of possible commands.
cmdlist = ['LED_1_ON',
           'LED_2_ON',
           'LED_3_ON',
           'LED_1_OFF',
           'LED_2_OFF',
           'LED_3_OFF'
           ]

# which pins to use (BCM mode)
pins = {'1': 18,
        '2': 19,
        '3': 20}

# translate str command to GPIO
states = {'ON': GPIO.HIGH,
          'OFF': GPIO.LOW}


def setup_hardware():
    """Sets up the GPIO pins on the RPi TCP-Server"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(list(pins.values()), GPIO.OUT)

    GPIO.output(list(pins.values()), GPIO.LOW)


def parse_cmd(cmd):
    """
    Parses a received str command and compares against
    the list of available commands
    """
    if cmd not in cmdlist:
        print('Command ' + cmd + ' unknown.')
        return NotImplementedError
    else:
        return cmd.split('_')


def toggle_led(cmd_parsed):
    """Toggles LED states according to received command"""
    GPIO.output(pins[cmd_parsed[1]], states[cmd_parsed[2]])
    print('Turned LED ' + cmd_parsed[1] + ' ' + cmd_parsed[2])
