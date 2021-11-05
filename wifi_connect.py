import network
import time
import socket
SSID="Nusri-Public"
PASSWORD=""
port=10000
wlan=None
listenSocket=None
def connectWifi(ssid,passwd):
    global wlan
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(ssid,passwd)
    while(wlan.ifconfig()[0]=='0.0.0.0'):
        time.sleep(1)
    return True
connectWifi(SSID,PASSWORD)
print('ip:',wlan.ifconfig()[0])