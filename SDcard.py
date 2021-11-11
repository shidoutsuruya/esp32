import machine,uos
sd =machine.SDCard(slot=2, sck=18, mosi=23, miso=19, cs=4)
uos.mount(sd,'/sd')
print(uos.listdir('/'))