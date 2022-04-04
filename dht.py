import Adafruit_DHT as dht
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# LED GPIO pins
red = 17
yellow = 18
green = 27

TIMING = 0.5

SENSOR = dht.DHT22
PIN = 4

def blink(ledColor):
    GPIO.output(ledColor, True)
    sleep(TIMING)
    GPIO.output(ledColor, False)
    sleep(TIMING)

while True:
    humidity, temp = dht.read_retry(SENSOR, PIN)
    
    if humidity is not None and temp is not None:
        
        print("Temp={:0.1f}*C".format(temp))
        print("Humidity={:0.1f}%".format(humidity))
        
        if(temp < 25):
            for i in range(0,3):
                blink(green)
        if(temp >= 25):
            for i in range(0,3):
                blink(yellow)
        if(temp >= 30):
            for i in range(0,3):
                blink(red)
        
        if(humidity < 80):
            for i in range(0,3):
                blink(red)
                print("Humidity too low, you mushrooms will dry out")
        
    else:
        print("failed to retreive data from the sensor")