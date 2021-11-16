from machine import Pin,SoftI2C
import time
#addresses

i2c=SoftI2C(scl=Pin(14),sda=Pin(12),freq=100000)

print(0x0f)
def RGBSet(R,G,B):
	date = []
	date.append(R)
	date.append(G)
	date.append(B)
	print(date)
	i2c.writeto_mem(0x0f,0x03,bytes(date))#第三个参数list，元素小于30个
while True:
    time.sleep(0.1)
    RGBSet(255,255,255)
    time.sleep(0.1)
    RGBSet(0,0,0)