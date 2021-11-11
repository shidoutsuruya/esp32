from machine import PWM,Pin,ADC
import time
Trig1 = Pin(13,Pin.OUT)
Echo1 = Pin(34,Pin.IN)
Trig2 = Pin(12,Pin.OUT)
Echo2 = Pin(35,Pin.IN)
speaker=Pin(14,Pin.OUT)
def pwm_change(pin,lst):
    for i in lst:   
        PWM(pin,freq=i,duty=1)
w=100
lst=[261]*w
lst2=[1000]*w
def ultra(Echo,Trig,sound_lst,name):
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
            pwm_change(speaker,sound_lst)
        else:
            pwm_change(speaker,[0])
            speaker.off()
        print(name+' Distance:',distance,'cm')
while True:
    ultra(Echo1,Trig1,lst,'trig1')
    time.sleep(0.1)
    ultra(Echo2,Trig2,lst2,'trig2')
    time.sleep(0.1)