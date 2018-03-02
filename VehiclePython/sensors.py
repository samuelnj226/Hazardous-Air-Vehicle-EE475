# code ideas taken from adafruit library for this sensor, but have been adapted.
# https://github.com/adafruit/Adafruit_CircuitPython_SGP30/blob/master/adafruit_sgp30.py

import smbus
import time
from micropython import const

#taken from example driver
#constants
_SGP30_DEFAULT_I2C_ADDR  = const(0x58)
_SGP30_FEATURESET        = const(0x0020)

_SGP30_CRC8_POLYNOMIAL   = const(0x31)
_SGP30_CRC8_INIT         = const(0xFF)
_SGP30_WORD_LEN          = const(2)

#class to control bus
class AirQualitySensor:

    def __init__(self):
        #setup bus
        self.bus = smbus.SMBus(0) # 0 indicates /dev/i2c-0



    #write data, then read back after delay
    def readFromCommand(self, data, delay, reply_size)
        #with self.bus
        if isinstance(data, list):
            self.bus.write_block_data(_SGP30_DEFAULT_I2C_ADDR, data[0], data[1:len(data)])
        else:
            self.bus.write_byte(_SGP30_DEFAULT_I2C_ADDR, data)

        time.delay(delay)

        data = read_block_data(_SGP30_DEFAULT_I2C_ADDR, reply_size)

    

