from machine import Pin
import time
def led_on(id,time_ms):
    p1=Pin(id,Pin.OUT)
    p1.on()#set pin tp 'on' high level
    #p1.value(1)#same as p1.on
    time.sleep_ms(time_ms)
    p1.off()
   
def get_pin_info(id):
    p2=Pin(id,Pin.IN)
    print(p2.value())
    
get_pin_info(2)
    
