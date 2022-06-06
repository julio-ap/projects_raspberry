import machine
import utime

i2c = machine.I2C(0, scl=machine.Pin(3), sda=machine.Pin(2), freq=200000)

direccion = hex(i2c.scan()[0])

print(direccion)