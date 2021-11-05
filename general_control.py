import machine
import esp
print(machine.freq())#get the current frequency of the CPU
esp.osdebug(None)#turn off debug message
print('flash size:',esp.flash_size())
print('flash user start:',esp.flash_user_start())
#print('erase:',esp.flash_erase(1))
import network
wlan=network.WLAN(network.STA_IF)#create station interface
wlan.active(True)#activate the interface
wifi=wlan.scan()#scan the surrounding wifi
wlan.isconnect()
wlan.connect('MY-COMPUTER','1234567890')
wlan.config('mac')