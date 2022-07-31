import RPi.GPIO as GPIO
from time import sleep
import pinout

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(0)

gpio_setup()
# Pins setup
relay1 = pinout.PIN_FANS_1

def start_fans(x):
    # startup for fans and let them run for x hours
    print(x)
    
    
try:
    GPIO.setup(relay1, GPIO.OUT)
    GPIO.output(relay1, 0)
    sleep(5)
    GPIO.output(relay1, 1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    
    
GPIO.cleanup()

