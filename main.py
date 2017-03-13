from ev3dev.ev3 import *

gy = GyroSensor()

#Put sensor in ANGLE mode
gy.mode('GYRO-ANG')

units = gy.units

while true:
	angle = gy.value()
	print(str(angle) + " " + units)


