import network
wlan = network.WLAN(network.STA_IF)


def scan():
    result = wlan.scan()
    for i in range(0, len(result)):
        print(result[i][0])


def scan_raw():
    print(wlan.scan())


def ifconfig():
    print(wlan.ifconfig([(ip, subnet, gateway, dns)]))


def set_mac_addr(addr):
    wlan.config(mac=addr)


def auto_connect_wifi():
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect('circuitspecialists.com', 'C!rCu!t!')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def connect(SSID, Password):
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect(SSID, Password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def set_phy(mode):
    wlan.phy_mode([mode])
