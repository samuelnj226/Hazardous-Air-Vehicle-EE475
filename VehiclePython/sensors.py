# code ideas taken from adafruit library for this sensor, but have been adapted.
# https://github.com/adafruit/Adafruit_CircuitPython_SGP30/blob/master/adafruit_sgp30.py

import smbus
import time

#constants
_SGP30_DEFAULT_I2C_ADDR  = 0x58
_SGP30_FEATURESET        = 0x0020

_SGP30_CRC8_POLYNOMIAL   = 0x31
_SGP30_CRC8_INIT         = 0xFF
_SGP30_WORD_LEN          = 2

#class to control bus
class AirQualitySensor:

    def __init__(self):
        #setup bus
        self.bus = smbus.SMBus(1) # 0 indicates /dev/i2c-0



    #write data, then read back after delay
    def readFromCommand(self, data, delay, reply_size)
        #with self.bus
        if isinstance(data, list):
            self.bus.write_block_data(_SGP30_DEFAULT_I2C_ADDR, data[0], data[1:len(data)])
        else:
            self.bus.write_byte(_SGP30_DEFAULT_I2C_ADDR, data)

        time.delay(delay)

        data = read_block_data(_SGP30_DEFAULT_I2C_ADDR, reply_size)

    #copied directlly from adafruit library
    def _generate_crc(self, data):
        """8-bit CRC algorithm for checking data"""
        crc = _SGP30_CRC8_INIT
        # calculates 8-Bit checksum with given polynomial
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ _SGP30_CRC8_POLYNOMIAL
                else:
                    crc <<= 1
        return crc & 0xFF

