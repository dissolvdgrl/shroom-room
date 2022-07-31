# NB: This script will only work on a Raspberry Pi.

# Import the DHT library for use with the DHT22
import Adafruit_DHT as dht

# Import the library to use the GPIO pins on the Raspberry Pi
import RPi.GPIO as GPIO

# Import the time library to use the sleep function
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the sensor type and GPIO pin to read data to use
DHT = dht.DHT22
PIN = 4

try:
    humidity, temp = dht.read_retry(DHT, PIN)
    
    if humidity is not None and temp is not None:

        # Send these to some DB at some interval
        print("Temp={:0.1f}*C".format(temp))
        print("Humidity={:0.1f}%".format(humidity))
        
        if temp < 14:
            print("Too cold.")
            # Do something here to warn about low
            # temperature and/or switch on a heater

        if temp > 22:
            print("Too hot.")
            # Do something here to warn about high
            # temperature and/or switch on a cooler
        
        if humidity < 80:
            print("Humidity too low")
            # Do something here to warn about low
            # humidity and/or switch on a humidifier

        if humidity == 100:
            print("Humidity is high enough")
            # Switch off humidifier

        
    else:
        print("failed to retreive data from the sensor")
except KeyboardInterrupt:
    GPIO.cleanup()


GPIO.cleanup() # clean up the GPIO pins when the program ends