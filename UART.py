from machine import UART
uart1=UART(1,baudrate=9600,tx=33,rx=32)
uart1.write('hello')
uart1.read(5)