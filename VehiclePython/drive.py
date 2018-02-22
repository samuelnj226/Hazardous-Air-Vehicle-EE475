# try catch block taken from example code found in library documentation
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

#set board mode
GPIO.setmode(GPIO.BOARD)

#setup motor control GPIOS
GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)

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


# for exit interrupt GPIO.cleanup()