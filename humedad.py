import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sh1 = 17

GPIO.setup(sh1, GPIO.IN)

def medirHumedad():
    valor1= GPIO.input(17)
    if valor1 == 0:
        print ("humedo")
    else:
        print("seco")
        
print ("obteniendo humedad")
while True :
    medirHumedad()
    time.sleep(2)