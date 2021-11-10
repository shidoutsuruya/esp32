from machine import PWM,Pin,ADC
import time
adc=ADC(Pin(34))
def pwm_change(pin,freq,duty):
    pwm=PWM(pin,freq=freq,duty=duty)
w=1000
lst=[261]*w+[293]*w+[329]*w+[349]*w+[392]*w
speaker=Pin(13,Pin.OUT,Pin.PULL_UP)
while True:
    if adc.read()>3000:
        for i in lst:   
            pwm_change(speaker,i,5)
        speaker.on()
    else:
        pwm_change(speaker,1,0)
        speaker.off()