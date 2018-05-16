import machine
import neo6mgps
import bme280
import mpu9250
from microWebSrv import MicroWebSrv
import os
import network
import utime


def init():
    global wlan
    wlan = network.WLAN(network.STA_IF)
    auto_connect_wifi(SSID='circuitspecialists.com', Password='')
    try:
        rocket_init()
        print("succesful to start")
    except:
        print("failed to start")


def rocket_init():
    bme_init()
    mpu9250_init()
    try:
        gps_init()
    except:
        print("GPS failed to init, please restart....")
        pass
    #httpserver_init()


def datavalues():
    global altitude
    altitude = bme.getAltitude_ft()
    global delta_altitude
    delta_altitude = 0.0
    global max_delta_altitude
    max_delta_altitude = 0.0
    global acceleration
    acceleration = 0.0
    global max_acceleration
    max_acceleration = 0.0
    global pressure
    pressure = 0.0
    delta_altitude = bme.getAltitude_ft() - altitude

    if (delta_altitude >= max_delta_altitude):
        max_delta_altitude = delta_altitude
    if (acceleration >= max_acceleration):
        max_acceleration = acceleration

    pressure = bme.getPressure()
    gps.update()
    gps.interpret_rmc()

    datavalues = [
        altitude, delta_altitude, max_delta_altitude, acceleration,
        max_acceleration, pressure, gps.latitude, gps.latitude_direction,
        gps.longitude, gps.longitude_direction, gps.speed,
        gps.getformatedUTC(-7)
    ]

    return datavalues


@MicroWebSrv.route('/sensordata')
def _httpHandlerSensorDataGet(httpClient, httpResponse):
    httpResponse.WriteResponseOk(
        headers=({
            'Cache-Control': 'no-cache'
        }),
        contentType='text/event-stream',
        contentCharset='UTF-8',
        content='data: {0}\n\n'.format(str(datavalues())))


def _acceptWebSocketCallback(webSocket, httpClient):
    print("WS ACCEPT")
    webSocket.RecvTextCallback = _recvTextCallback
    webSocket.RecvBinaryCallback = _recvBinaryCallback
    webSocket.ClosedCallback = _closedCallback


def _recvTextCallback(webSocket, msg):
    print("WS RECV TEXT : %s" % msg)
    webSocket.SendText("Reply for %s" % msg)


def _recvBinaryCallback(webSocket, data):
    print("WS RECV DATA : %s" % data)


def _closedCallback(webSocket):
    print("WS CLOSED")


def httpserver_init():
    global server
    server = MicroWebSrv(webPath='www/')
    server.MaxWebSocketRecvLen = 256
    server.WebSocketThreaded = False
    server.AcceptWebSocketCallback = _acceptWebSocketCallback
    server.Start(threaded=False)


def gps_init():
    global gps
    gps = neo6mgps.NEO6MGPS(baudrate=9600)
    gps.update()
    gps.interpret_rmc()


def mpu9250_init():
    global i2c_mpu9250
    global sensor
    i2c_mpu9250 = machine.I2C(scl=machine.Pin(26), sda=machine.Pin(25))
    sensor = mpu9250.MPU9250(i2c=i2c_mpu9250)
    sensor.calibrate_MPU9250()


def calculate_acceleration():
    x_acceleration = float(sensor.acceleration[0])
    y_acceleration = float(sensor.acceleration[1])
    z_acceleration = float(sensor.acceleration[2])


def bme_init():
    global i2c_bme280
    global bme
    i2c_bme280 = machine.I2C(scl=machine.Pin(33), sda=machine.Pin(32))
    bme = bme280.BME280(i2c=i2c_bme280)


def auto_connect_wifi(SSID, Password):
    if (not wlan.isconnected()):
        print('connecting to network...')
        wlan.active(True)
        wlan.connect(SSID, Password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
