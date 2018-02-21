/* 
 * File:   accelerometer.h
 * Author: Sam
 *
 * Created on February 13, 2018, 4:54 PM
 * Code ideas taken from Adafruit driver for this accelerometer.
 */

#ifndef ACCELEROMETER_H
#define	ACCELEROMETER_H

#include "mcc_generated_files/drivers/i2c_master.h"
#define _XTAL_FREQ 16000000
#include <p18f25k22.h>
#include <xc.h>
#include <stdio.h>
#include <stdint.h> //for uint8_t datatype
#include <p18cxxx.h>
#include <string.h>
#include <stdlib.h>


// taken from adafruit driver//
#define MMA8451_DEFAULT_ADDRESS 0x1D

#define MMA8451_REG_OUT_X_MSB     0x01
#define MMA8451_REG_SYSMOD        0x0B
#define MMA8451_REG_XYZ_DATA_CFG  0x0E
#define MMA8451_REG_PL_STATUS     0x10
#define MMA8451_REG_PL_CFG        0x11
#define MMA8451_REG_CTRL_REG1     0x2A
#define MMA8451_REG_CTRL_REG2     0x2B
#define MMA8451_REG_CTRL_REG4     0x2D
#define MMA8451_REG_CTRL_REG5     0x2E

// taken from adafruit driver//
typedef enum
{
  MMA8451_RANGE_8_G           = 0b10,   // +/- 8g
  MMA8451_RANGE_4_G           = 0b01,   // +/- 4g
  MMA8451_RANGE_2_G           = 0b00    // +/- 2g (default value)
} mma8451_range_t;

typedef struct {
    int16_t x;
    int16_t y;
    int16_t z;
} accelerometer_data_t;

void ACCELEROMETER_Initialize(void);
void write_register(uint8_t reg, uint8_t data);
uint8_t read_register(uint8_t reg);
accelerometer_data_t read_xyzvalues(void);

#endif	/* ACCELEROMETER_H */

