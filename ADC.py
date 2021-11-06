from machine import ADC,Pin
import time
adc=ADC(Pin(34))
def attenuate(db=0):
    """
    change the wider possible input voltage range
    """
    if db==2.5:
        adc.atten(ADC.ATTN_2_5DB)#0-1.34v
        print('attentuation:',db)
    elif db==6:
        adc.atten(ADC.ATTN_6DB)#0-2.00v
        print('attentuation:',db)
    elif db==11:
        adc.atten(ADC.ATTN_11DB)#0-3.6v
        print('attentuation:',db)
    else:
        adc.atten(ADC.ATTN_0DB)#0-1v
        print('attentuation:',0)
def bit_width(width=12):
    """
    sample bit width [9,10,11,12]
    """
    if width==9:
        adc.width(ADC.WIDTH_9BIT)
    elif width==10:
        adc.width(ADC.WIDTH_10BIT)
    elif width==11:
        adc.width(ADC.WIDTH_11BIT)
    else:
        adc.width(ADC.WIDTH_12BIT)
    
while True:
    print(adc.read())
    time.sleep(0.1)

