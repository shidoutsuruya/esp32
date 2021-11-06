from machine import Pin
import time
Trig = Pin(13,Pin.OUT)
Echo = Pin(12,Pin.IN)
led=Pin(2,Pin.OUT)
while True:
    while(Echo.value()==0):
        Trig.value(1)
        time.sleep_us(20)
        Trig.value(0)
    if(Echo.value()==1):
        ts=time.ticks_us()
        while(Echo.value()==1):
            pass
        te=time.ticks_us()
        tc=te-ts
        distance=(tc*0.034)/2
    if distance<100:
        led.on()
    else:
        led.off()
    print('Distance:',distance,'cm')
    time.sleep(0.01)
