import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sh1 = 17
sh2 = 27
sh3 = 22

GPIO.setup(sh2, GPIO.IN)
GPIO.setup(sh1, GPIO.IN)
GPIO.setup(sh3, GPIO.IN)

def humedad1(sh1):
    if GPIO.input(sh1):
        print("h1=0")
    else:
        print("h1=1")
    


def humedad2(sh2):
    if GPIO.input(sh2):
        print("h2=0")
    else:
        print("h2=1")
    


def humedad3(sh3):
    if GPIO.input(sh3):
        print("h3=0")
    else:
        print("h3=1")
        
GPIO.add_event_detect(sh2, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sh2, humedad2)        
GPIO.add_event_detect(sh1, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sh1, humedad1)    
GPIO.add_event_detect(sh3, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sh3, humedad3)
        

while True :
    time.sleep(1)