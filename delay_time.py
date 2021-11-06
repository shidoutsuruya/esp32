import time
time.sleep_ms(500)#calculate time in ms
time.sleep_us(1000)#calculate time in us
start=time.ticks_ms()
time.sleep(1)
delta=time.ticks_diff(time.ticks_ms(),start)#calculate time
print(delta)

