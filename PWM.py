from machine import Pin,PWM
import time
def pulse_width_modulation(id):
    pwm=PWM(Pin(id))
    print('pwm frequency:',pwm.freq())#frequency show the color change
    print('pwm current duty cycle:',pwm.duty())#duty show lightness 
def pwm_change(id,freq,duty):
    pwm=PWM(Pin(id),freq=freq,duty=duty)
    

    