from machine import Pin,SoftI2C
import time
#addresses
i2c=SoftI2C(scl=Pin(14),sda=Pin(12),freq=100000)
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

def I2CReadByte():
    global i2c_addr
    time.sleep(0.05)
    Read_result=i2c.readfrom_mem(i2c_addr,asr_result,8)
    return Read_result
def RGBSet(R,G,B):
    date = []
    date.append(R)
    date.append(G)
    date.append(B)
    i2c.writeto_mem(0x0f,0x03,bytes(date))
def AsrAddWords(idnum,str):
    global i2c_addr
    global asr_add_word_addr
    words = []
    words.append(idnum)
    for  alond_word in str:
        words.append(ord(alond_word))
    print(words)
    i2c.writeto_mem(i2c_addr,asr_add_word_addr,bytes(words))#three list <1
    time.sleep(1)
def sound_on():
    i2c.writeto_mem(0x0f,0x09,bytes([1]))
def sound_off():
	i2c.writeto_mem(0x0f,0x09,bytes([0]))
if 1:
    i2c.writeto_mem(i2c_addr, asr_mode_addr,bytes(0x01))#set
    time.sleep(0.1)
    AsrAddWords(0,"kai deng")
    AsrAddWords(1,"xiao deng")	
    AsrAddWords(2,"guan deng")	
i2c.writeto_mem(i2c_addr, asr_rec_gain_addr,bytes([0x44]))#set resolution
while True:
    result=I2CReadByte()
    print(result)
    if result!=b'\xff\xff\xff\xff\xff\xff\xff\xff':
        for _ in range(3):
            time.sleep(0.1)
            RGBSet(255,255,255)
            sound_on()
            time.sleep(0.1)
            RGBSet(0,0,0)
            sound_off()
    else:
        RGBSet(0,0,0)
        sound_off()