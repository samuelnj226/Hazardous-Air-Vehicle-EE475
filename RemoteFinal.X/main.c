/**
  Generated Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This is the main file generated using PIC10 / PIC12 / PIC16 / PIC18 MCUs

  Description:
    This header file provides implementations for driver APIs for all modules selected in the GUI.
    Generation Information :
        Product Revision  :  PIC10 / PIC12 / PIC16 / PIC18 MCUs - 1.65
        Device            :  PIC18F25K22
        Driver Version    :  2.00
*/

/*
    (c) 2016 Microchip Technology Inc. and its subsidiaries. You may use this
    software and any derivatives exclusively with Microchip products.

    THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
    EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
    WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
    PARTICULAR PURPOSE, OR ITS INTERACTION WITH MICROCHIP PRODUCTS, COMBINATION
    WITH ANY OTHER PRODUCTS, OR USE IN ANY APPLICATION.

    IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
    WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
    BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
    FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
    ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
    THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.

    MICROCHIP PROVIDES THIS SOFTWARE CONDITIONALLY UPON YOUR ACCEPTANCE OF THESE
    TERMS.
*/

#include "mcc_generated_files/mcc.h"
#include "accelerometer.h"
#define _XTAL_FREQ 16000000
#include <p18f25k22.h>
#include <xc.h>
#include <stdio.h>
#include <stdint.h> //for uint8_t datatype
#include <p18cxxx.h>
#include <string.h>
#include <stdlib.h>

//UART METHODS
void Send_UART(char data){
    EUSART1_Write((uint8_t) data);
}

void printString() {
    char welcome[50] = "\n\rGOT HERE. \n\r";
    for (int i = 0; i < 50; i++ ) {
        EUSART1_Write(welcome[i]);
        __delay_ms(100);
    }
}

/*
                         Main application
 */
void main(void) {
    accelerometer_data_t data;
    
    // Initialize the device
    SYSTEM_Initialize();

    // Enable the Global Interrupts
    INTERRUPT_GlobalInterruptEnable();
    
    // Enable the Peripheral Interrupts
    INTERRUPT_PeripheralInterruptEnable();
    
    ACCELEROMETER_Initialize();
    
    //take out later
    //printString();
    
    while (1) {
        data = read_xyzvalues();
        __delay_ms(100);
        //printf("\n\rValues are, x: %d, y: %d, z: %d", temp, temp, data.z);
        
        EUSART1_Write(data.x & 0xff);
        __delay_ms(5);
        EUSART1_Write((data.x>>8) & 0xff);
        __delay_ms(5);
        EUSART1_Write(data.y & 0xff);
        __delay_ms(5);
        EUSART1_Write((data.y>>8) & 0xff);
        __delay_ms(5);
        EUSART1_Write(data.z & 0xff);
        __delay_ms(5);
        EUSART1_Write((data.z>>8) & 0xff);
        __delay_ms(5);
        printf("\r");
        __delay_ms(5);
        printf("\n");
    }
}
/**
 End of File
*/