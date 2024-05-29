#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick 
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
brick = EV3Brick()


# Write your program here.
brick.speaker.beep()
#Inicializa el motor en el Puerto A
motora=Motor (Port.A)
motorb=Motor (Port.B)

#Corre el motor a 500 grados por seg a un angulo de 90 grados
motora.run_target(5000, 90)
motorb.run_target(5000,180)

brick.speaker.beep(1000,500)
