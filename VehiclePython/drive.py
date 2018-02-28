# try catch block taken from example code found in library documentation
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

import serial
import sys
import signal
import struct

try:
    ser = serial.Serial(
        port='/dev/rfcomm0',
        baudrate=115200,
        parity='N',
        stopbits=1,
        bytesize=8
    )
    print('serial port open')
except serial.serialException:
    serial.Serial('/dev/rfcomm0').close()
    print('serial port not opened')

#set board mode
GPIO.setmode(GPIO.BOARD)

#setup motor enable control (for direction)
gpio_channels1 = [35, 36] 
gpio_channels2 = [37, 38]
GPIO.setup(gpio_channels1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(gpio_channels2, GPIO.OUT, initial=GPIO.HIGH)

# initialize PWM for motor speed control
gpio_pwm_channels = [31, 32]
GPIO.setup(gpio_pwm_channels, GPIO.OUT)
rightPWM = GPIO.PWM(31, 10000)
leftPWM = GPIO.PWM(32, 10000)

leftDuty = 0
rightDuty = 0

rightPWM.start(0)
leftPWM.start(0)

#close GPIOs and serial port (interupt)
def sigterm_handler(_signo, _stack_frame):
    rightPWM.ChangeDutyCycle(0)
    leftPWM.ChangeDutyCycle(0)
    rightPWM.stop()
    leftPWM.stop()
    GPIO.cleanup()
    ser.close()
    print("exiting...")
    sys.exit(0)

#set interrupt for sigterm and sigint
signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigterm_handler)



'''
while (1)
    y positive is forward
    x positive is right

    y from 200 to 1600 controls forward motion

    # set forward speed
    if y < 200
        duty cycle right = 0
        duty cycle left = 0
    else if y > 1600
        duty cycle right = 100
        duty cycle left = 100
    else
        duty cycle right = y/1600
        duty cycle left = y/1600

    # set turn format

    #right turn
    if x > 200
        duty cycle right = duty cycle right * (4000 - x)/4000
    else if x < -200 #left turn
        duty cycle left = duty cycle right * (4000 - x)/4000



'''
ser.readline()
while 1:
    command = ser.readline()
    unpackedCommand = struct.unpack('hhhh', command);
    x = unpackedCommand[0]
    y = unpackedCommand[1]
    z = unpackedCommand[2]


    # set forward speed
    if y < 200:
        rightDuty = 0
        leftDuty = 0
    elif y > 1600:
        rightDuty = 100
        leftDuty = 100
    else:
        rightDuty = y/1600 * 100
        leftDuty = y/1600 * 100
        
    # set turn format
    #right turn
    if x > 200:
        rightDuty = rightDuty * (4000 - x)/4000
    elif x < -200: #left turn
        leftDuty = leftDuty * (4000 - x)/4000

    rightPWM.ChangeDutyCycle(rightDuty)
    leftPWM.ChangeDutyCycle(leftDuty)

    print(unpackedCommand)
    print(rightDuty)
    print(leftDuty)

    

