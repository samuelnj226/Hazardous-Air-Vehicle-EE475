# try catch block taken from example code found in library documentation
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

import serial
import sys
import signal

#close GPIOs and serial port
def sigterm_handler(_signo, _stack_frame):
    GPIO.cleanup()
    ser.close()
    print("exiting...")
    sys.exit(0)

#set interrupt for sigterm
signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigterm_handler)

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

#setup motor control GPIOS channel 11 and 12
gpio_channels1 = [35, 36] 
gpio_channels2 = [37, 38]
GPIO.setup(gpio_channels1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(gpio_channels2, GPIO.OUT, initial=GPIO.HIGH)

# initialize connectiong with the emulated serial port for bluetooth
# initialize PWM and GPIOs for motor control

'''
while (1)
    get x y z;
    ignore z value;
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
while 1:
     print (ser.read(10))
    


# for exit interrupt GPIO.cleanup()
GPIO.cleanup()
ser.close()
