from machine import Pin,SoftI2C
import time
#addresses

i2c_addr = 0x0f   
asr_add_word_addr  = 0x01   
asr_mode_addr  = 0x02   
asr_rgb_addr = 0x03   		
asr_rec_gain_addr  = 0x04                                          
asr_clear_addr = 0x05  
asr_key_flag = 0x06  
asr_voice_flag = 0x07   
asr_result = 0x08  
asr_buzzer = 0x09 
asr_num_cleck = 0x0a 
i2c=SoftI2C(scl=Pin(14),sda=Pin(12),freq=100000)
def RGBSet(R,G,B):
	date = []
	date.append(R)
	date.append(G)
	date.append(B)
	print(date)
	i2c.writeto_mem(0x0f,0x03,bytes(date))
def sound_on():
    i2c.writeto_mem(0x0f,0x09,bytes([1]))
def sound_off():
	i2c.writeto_mem(0x0f,0x09,bytes([0]))
while True:
    time.sleep(0.1)
    RGBSet(255,255,255)
    sound_on()
    time.sleep(0.1)
    RGBSet(0,0,0)
    sound_off()
    