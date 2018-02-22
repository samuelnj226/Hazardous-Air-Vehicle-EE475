print "hello world"

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
