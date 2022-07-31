'''
    Pin out setup for the Raspberry Pi 3 B+
    connecting to a relay module with any
    number of channels as required.

    Pinout based on the GPIO numbers:
        GPIO.setmode(GPIO.BCM)

    Please see the README for hardware details.
'''

PIN_H_SENSOR = 17
PIN_FANS_1 = 2 # corresponds to my relay's 1st channel
PIN_HUMIDIFIER = 3 # corresponds to my relay's 2nd channel