import machine
import esp32
from machine import Pin
from time import sleep
print('hello')
wake1 = Pin(13, mode = Pin.IN)#connect a button

esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)
print('Im awake. Going to sleep in 3 seconds')
sleep(3)
print('Going to sleep now')
machine.deepsleep()