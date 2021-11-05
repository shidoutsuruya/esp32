import network
ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid='ESP32_MAX') # set the ESSID of the access point
ap.config(max_clients=10) # set how many clients can connect to the network
ap.active(True)         # activate the interface
print('ESP32_MAX is open')