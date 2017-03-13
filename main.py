from ev3dev.ev3 import *
from time import sleep

gy = GyroSensor()

#Put sensor in ANGLE mode
gy.mode='GYRO-ANG'

units = gy.units

while True:
	angle = gy.value()
	print(str(angle) + " " + units)
	sleep(0.2)

