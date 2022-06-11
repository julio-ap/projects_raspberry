import RPi.GPIO as GPIO
import time
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

GPIO.setmode(GPIO.BCM)

sh1 = 17
sh2 = 27
sh3 = 22

GPIO.setup(sh2, GPIO.IN)
GPIO.setup(sh1, GPIO.IN)
GPIO.setup(sh3, GPIO.IN)

def humedad1(sh1):
    v1 =GPIO.input(sh1)
    if v1==0:
        print("h1=0")
        lcd.text("REGADO NECESARIO (1)",1)
    else:
        print("h1=1")
        lcd.text("HUMEDAD OPTIMA",1)
    


def humedad2(sh2):
    v2 =GPIO.input(sh2)
    if v2==0:
        print("h2=0")
        lcd.text("REGADO NECESARIO (2)",2)

    else:
        print("h2=1")
        lcd.text("HUMEDAD OPTIMA",2)


def humedad3(sh3):
    v3 =GPIO.input(sh3)
    if v3==0:
        print("h3=0")
        lcd.text("REGADO NECESARIO (3)",3)
    else:
        print("h3=1")
        lcd.text("HUMEDAD OPTIMA",3)
        
        
        
GPIO.add_event_detect(sh2, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sh2, humedad2)        
GPIO.add_event_detect(sh1, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sh1, humedad1)    
GPIO.add_event_detect(sh3, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sh3, humedad3)
        


while True :
    time.sleep(1)