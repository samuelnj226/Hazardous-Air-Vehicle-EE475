# code ideas taken from adafruit library for this sensor, but have been adapted.
# https://github.com/adafruit/Adafruit_CircuitPython_SGP30/blob/master/adafruit_sgp30.py

import smbus
import time

import sensors

_SGP30_CRC8_POLYNOMIAL   = 0x31
_SGP30_CRC8_INIT         = 0xFF

sensor = sensors.AirQualityTempSensor()



'''
#copied directlly from adafruit library
def _generate_crc(data):
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

while 1:
    bus.write_i2c_block_data(0x58, 0x20, [0x2f])
    time.sleep(0.01)
    data = bus.read_i2c_block_data(0x58, 0)
    print(data)
    print(_generate_crc([0, 0]))
    print(_generate_crc([0, 100]))
    print(_generate_crc([202, 154]))
'''


