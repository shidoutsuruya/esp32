from machine import Pin,SoftI2C
import utime
i2c=SoftI2C(scl=Pin(5),sda=Pin(4),freq=100000)
print(i2c.scan())
a=i2c.readfrom(0x48,5)
while True:
    utime.sleep_ms(1000)
    print(a)