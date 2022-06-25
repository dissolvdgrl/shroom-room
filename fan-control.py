import RPi.GPIO as GPIO
import Adafruit_DHT as dht
from time import sleep

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(0)

gpio_setup()
# Pins setup
relay1 = 2
relay2 = 3
SENSOR = dht.DHT22
dhtPin = 17
    
    
try:
    while True:
        humidity, temp = dht.read_retry(SENSOR, dhtPin)
        GPIO.setup(relay1, GPIO.OUT)
        GPIO.setup(relay2, GPIO.OUT)
        
        temp = float(temp)
    
        if humidity is not None and temp is not None:
            print("Temp={:0.1f}*C".format(temp))
            print("Humidity={:0.1f}%".format(humidity))
        
        if temp >= 16.7:
            GPIO.output(relay1, 0)
            GPIO.output(relay2, 0)
        elif temp < 16.6:
            GPIO.output(relay1, 1)    
            GPIO.output(relay2, 1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    
    
GPIO.cleanup()

