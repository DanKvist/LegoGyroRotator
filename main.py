#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts

gy = GyroSensor()
lcd = Screen()
dispFont = fonts.load('luBS24')


#Put sensor in ANGLE mode
gy.mode='GYRO-ANG'

units = gy.units

while True:
	lcd.clear()
	angle = gy.value()
	lcd.draw.text((30,60), str(angle) + " " + units, font=dispFont)
	lcd.update()
	sleep(0.5)

