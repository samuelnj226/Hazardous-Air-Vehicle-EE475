#include "accelerometer.h"

//
void ACCELEROMETER_Initialize(void) {
    
    write_register(MMA8451_REG_CTRL_REG2, 0x40); // reset
    
    __delay_ms(100);

    // wait for reset to clear
    while (read_register(MMA8451_REG_CTRL_REG2) & 0x40);

    // enable 4G range
    write_register(MMA8451_REG_XYZ_DATA_CFG, MMA8451_RANGE_4_G);
    // High res
    write_register(MMA8451_REG_CTRL_REG2, 0x02);
    // DRDY on INT1
    write_register(MMA8451_REG_CTRL_REG4, 0x01);
    write_register(MMA8451_REG_CTRL_REG5, 0x01);

    // Turn on orientation config
    write_register(MMA8451_REG_PL_CFG, 0x40);

    // Activate at max rate, low noise mode
    write_register(MMA8451_REG_CTRL_REG1, 0x01 | 0x04);
}

//write data to given register
void write_register(uint8_t reg, uint8_t data) {
    static i2c_error_t status; //status of the bus
    static uint8_t buffer[2];
    
    //set data to send
    buffer[0] = reg;
    buffer[1] = data;
    i2c_open(MMA8451_DEFAULT_ADDRESS); //open remote node
    i2c_setBuffer(buffer, 2); //set the buffer
    
    //send data
    status = i2c_masterWrite();
    status = i2c_close();
}


//read one value from given register
uint8_t read_register(uint8_t reg){
    static i2c_error_t status; //status of the bus
    static volatile uint8_t receivebuffer[1];
   
    //open device
    i2c_open(MMA8451_DEFAULT_ADDRESS); //open remote node
    
    //reopen again, read
    //i2c_open(MMA8451_DEFAULT_ADDRESS); //open remote node
    i2c_setBuffer(receivebuffer, 1); //set the buffer
    
    //receive data
    status = i2c_masterAccelRead(reg);
    
    //close channel
    status = i2c_close();
    
    return receivebuffer[0];
}

//read values from the registers on the device
accelerometer_data_t read_xyzvalues(void){
    static i2c_error_t status; //status of the bus
    static volatile uint8_t readbuffer[6];
    accelerometer_data_t sensorData;
    
    //reopen again, read
    i2c_open(MMA8451_DEFAULT_ADDRESS); //open remote node
    i2c_setBuffer(readbuffer, 6); //set the buffer
    
    //receive data
    status = i2c_masterAccelRead(MMA8451_REG_OUT_X_MSB);
    
    //close channel
    status = i2c_close();
    
    sensorData.x = readbuffer[0];
    sensorData.x <<= 8; 
    sensorData.x |= readbuffer[1];
    sensorData.x >>= 2;
    
    sensorData.y = readbuffer[2];
    sensorData.y <<= 8; 
    sensorData.y |= readbuffer[3];
    sensorData.y >>= 2;
    
    sensorData.z = readbuffer[4];
    sensorData.z <<= 8; 
    sensorData.z |= readbuffer[5];
    sensorData.z >>= 2;
    
    return sensorData;
};
