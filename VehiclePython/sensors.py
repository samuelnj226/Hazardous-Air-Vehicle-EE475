# code ideas taken from adafruit library for this sensor, but have been adapted.
# for the raspberry pi based on the spec sheet and different function calls
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

        #check that it is a SGP30 sensor
        features = self.readFromCommand([0x20, 0x2F], 0.01, 1)
        if features[0] != _SGP30_FEATURESET
            raise RuntimeError("could not find sensor")

        #initialize IAQ algorithm



    #write command, and then read back 3 * reply_size bytes
    #then return an array of size reply_size containing 16-bit numbers
    #after checking the CRC codes
    def readFromCommand(self, command, delay, reply_size)
        #with self.bus
        self.bus.write_i2c_block_data(_SGP30_DEFAULT_I2C_ADDR, command[0], command[1:len(command)])

        time.delay(delay)

        data = read_i2c_block_data(_SGP30_DEFAULT_I2C_ADDR, 0)

        #check CRC here
        result = []
        for i in range(reply_size):
            if self._generate_crc([data[3*i], data[3*i+1]]) != data[3*i+2]
                raise RuntimeError('CRC Error');
            result.append(data[3*i] << 8 | data[3*i+1])

        return result

    #copied directlly from adafruit library
    # https://github.com/adafruit/Adafruit_CircuitPython_SGP30/blob/master/adafruit_sgp30.py
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

