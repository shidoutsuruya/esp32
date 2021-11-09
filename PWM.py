from machine import Pin,PWM
import time
def pulse_width_modulation(pin):
    pwm=PWM(pin)
    print('pwm frequency:',pwm.freq())#frequency show the color change
    print('pwm current duty cycle:',pwm.duty())#duty show lightness 
def pwm_change(pin,freq,duty):
    pwm=PWM(pin,freq=freq,duty=duty)
while True:   
    pin=Pin(5)
    pwm_change(pin,1000,512)
    pin.on()
    