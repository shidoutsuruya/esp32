import os
from machine import Pin,SoftSPI,SDCard
spi=SoftSPI(baudrate=100000,polarity=1,phase=0,miso=Pin(13),mosi=Pin(12),sck=Pin(14))
print(spi.read(10))
