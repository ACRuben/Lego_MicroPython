#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

brick=EV3Brick()

left_motor=Motor(Port.A)
right_motor=Motor(Port.B)

robot=DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
robot.straight(500)
brick.speaker.beep()

robot.straight(-500)
brick.speaker.beep()

robot.turn(360)
brick.speaker.beep()

robot.turn(-360)
brick.speaker.beep()
