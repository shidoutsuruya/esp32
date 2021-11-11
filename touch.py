import machine
from machine import TouchPad, Pin
import esp32
t = TouchPad(Pin(14))
t.config(500)               # configure the threshold at which the pin is considered touched
esp32.wake_on_touch(True)
print('hello')
machine.lightsleep()  