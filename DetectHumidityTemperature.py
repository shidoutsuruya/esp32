import dht
import machine
from machine import Pin 
import utime
d=dht.DHT11(Pin(16))
d.measure()
while True:
    utime.sleep_ms(500)
    print('temp:',d.temperature(),'humidity:',d.humidity())
    
