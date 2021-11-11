from machine import UART,Pin 
import utime
uart=UART(2,baudrate=115200,rx=16,tx=17,timeout=10)
count=1
while True:
    print(f'++++connenct:{count}\n')
    uart.write(f'hello {count}')
    utime.sleep_ms(1000)
    if uart.any():
        print(f'Echo Byte:{uart.readline()}')
    count+=1
    print('-'*90)

    