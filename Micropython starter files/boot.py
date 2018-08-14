try:
    exec(open("bash_commands.py").read())
except:
    pass

try:
    exec(open("main.py").read())
    init()
except:
    ## recover board on failure of main script
    import esp
    import webrepl
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, Password)
    utime.sleep(3)
    webrepl.start()