from machine import Pin
import time
p0=Pin(13,Pin.OUT)
while True:
    p0.value(1)
    time.sleep(3)
    p0.value(0)
    time.sleep(3)