import main
import esp
import webrepl
import network

SSID = ""
Password = ""

try:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, Password)
    utime.sleep(3)
    webrepl.start()
    main_thread = main.MAIN()
except:
    pass