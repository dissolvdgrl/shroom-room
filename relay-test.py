import RPi.GPIO as GPIO
import Adafruit_DHT as dht
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

relay1 = 2
relay2 = 3
relay3 = 4
SENSOR = dht.DHT22
dhtPin = 17

GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
    
    
try:
    while True:
        humidity, temp = dht.read_retry(SENSOR, dhtPin)        
        
        temp = float(temp)
    
        if humidity is not None and temp is not None:
            print("Temp={:0.1f}*C".format(temp))
            print("Humidity={:0.1f}%".format(humidity))
        
        if temp >= 14:
            GPIO.output(relay1, 0)
            GPIO.output(relay2, 0)
            GPIO.output(relay3, 0)
        elif temp < 14:
            GPIO.output(relay1, 1)    
            GPIO.output(relay2, 1)    
            GPIO.output(relay3, 1)
            
except KeyboardInterrupt:
    GPIO.output(relay1, 1)    
    GPIO.output(relay2, 1)
    GPIO.output(relay3, 1)
    GPIO.cleanup()
    
    
GPIO.cleanup()
