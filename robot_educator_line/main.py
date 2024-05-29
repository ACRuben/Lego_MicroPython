#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick 
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
coche = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light threshold. Choose values based on your measurements.
BROWN = 9
WHITE = 86
threshold = (BROWN + WHITE) / 2

# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 100
if(tresholw != WHITE)
{
    coche = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
}

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
else{

PROPORTIONAL_GAIN = 1.2

# Start following the line endlessly.
while True:
    # Calculate the deviation from the threshold.
    deviation = line_sensor.reflection() - threshold

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    coche.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    wait(10)
}