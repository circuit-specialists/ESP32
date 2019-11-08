#!/usr/bin/python
"""
written by Jake Pring from CircuitSpecialists.com
licensed as GPLv3
"""

import machine

class ESP8266:
    def __init__(self):
        # actual pin markings
        #self.S3 = self.GPIO10
        #self.S2 = self.GPIO9
        self.D0 = 16
        self.D1 = 5
        self.D2 = 4
        self.D3 = 0
        self.D4 = 2
        self.D5 = 14
        self.D6 = 12
        self.D7 = 13
        self.D8 = 15
        self.A0 = 17

class ESP32:
    def __init__(self):
        # Serial 0
        self.RX0 = 1
        self.TX0 = 3
        self.RTS0 = 22
        self.CTS0 = 19

        # Serial 1
        self.RX1 = 9
        self.TX1 = 10
        self.RTS1 = 11
        self.CTS1 = 6

        # Serial 2
        self.RX2 = 16
        self.TX2 = 17
        self.RTS2 = 7
        self.CTS2 = 8

        # SPI Pins (connected to onboard flash)
        self.SDCLK = 6
        self.SD0 = 7
        self.SD1= 8
        self.SD2 = 9
        self.SD3 = 10
        self.SDCMD = 11

        # ?????????????????????????
        self.VP = 36
        # no 37, 38??
        self.VN = 39

        # ADC1
        self.ADC1_0 = 36
        self.ADC1_3 = 39
        self.ADC1_6 = 34
        self.ADC1_7 = 35

        # ADC2
        self.ADC2_0 = 4
        self.ADC2_1 = 0
        self.ADC2_2 = 2
        self.ADC2_3 = 15
        self.ADC2_4 = 13
        self.ADC2_5 = 12
        self.ADC2_6 = 14
        self.ADC2_7 = 27
        self.ADC2_8 = 25
        self.ADC2_9 = 26
        
        # DAC
        self.DAC_1 = 25
        self.DAC_2 = 26

        # Digital/GPIO Pins
        self.D0 = 0
        self.D2 = 2
        self.D4 = 4
        self.D5 = 5
        self.D12 = 12
        self.D13 = 13
        self.D14 = 14
        self.D15 = 15
        self.D18 = 18
        self.D19 = 19
        # no 20??
        self.D21 = 21
        self.D22 = 22
        self.D23 = 23
        # no 24??
        self.D25 = 25
        self.D26 = 26
        self.D27 = 27
        # no 28, 29, 30, 31??
        self.D32 = 32
        self.D33 = 33
        self.D34 = 34
        self.D35 = 35
        
        
        
        
        
        