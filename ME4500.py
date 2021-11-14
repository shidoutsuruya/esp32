from machine import PWM,Pin,ADC
import time
Echo1 = Pin(36,Pin.IN)
Trig1 = Pin(13,Pin.OUT)
Echo2 = Pin(39,Pin.IN)
Trig2 = Pin(12,Pin.OUT)
Echo3 = Pin(34,Pin.IN)
Trig3 = Pin(14,Pin.OUT)
Echo4 = Pin(35,Pin.IN)
Trig4 = Pin(27,Pin.OUT)
Echo5 = Pin(32,Pin.IN)
Trig5 = Pin(26,Pin.OUT)
Echo6 = Pin(33,Pin.IN)
Trig6 = Pin(25,Pin.OUT)
Echo7 = Pin(23,Pin.IN)
Trig7 = Pin(22,Pin.OUT)
Echo8 = Pin(2,Pin.IN)
Trig8 = Pin(4,Pin.OUT)
Echo9 = Pin(19,Pin.IN)
Trig9 = Pin(18,Pin.OUT)
speaker=Pin(21,Pin.OUT)
def pwm_change(pin,lst):
    for i in lst:   
        PWM(pin,freq=i,duty=1)
w=25
high=[523]*w
middle=[261]*w
low=[130]*w  
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
    ultra(Echo1,Trig1,high,'trig1')
    time.sleep_ms(100)
    ultra(Echo2,Trig2,high,'trig2')
    time.sleep_ms(100)
    ultra(Echo3,Trig3,high,'trig3')
    time.sleep_ms(100)
    ultra(Echo4,Trig4,middle,'trig4')
    time.sleep_ms(100)
    ultra(Echo5,Trig5,middle,'trig5')
    time.sleep_ms(100)
    ultra(Echo6,Trig6,middle,'trig6')
    time.sleep_ms(100)
    ultra(Echo7,Trig7,low,'trig7')
    time.sleep_ms(100)
    ultra(Echo8,Trig8,low,'trig8')
    time.sleep_ms(100)
    ultra(Echo9,Trig9,low,'trig9')
    time.sleep_ms(100)
   
    