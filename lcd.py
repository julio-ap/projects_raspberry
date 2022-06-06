from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    lcd.text("Hello245,", 1)
    lcd.text("Raspberry Piipi!", 2)
    lcd.text("probando,", 3)
    lcd.text("tengo hambre", 4)

    pause()

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
