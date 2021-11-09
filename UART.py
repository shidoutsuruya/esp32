from machine import UART
uart=UART(1,baudrate=9600,tx=1,rx=3)
print(uart.read())