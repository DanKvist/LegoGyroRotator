#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts

gy = GyroSensor()
us = UltrasonicSensor()
lcd = Screen()
dispFont = fonts.load('luBS24')


#Put sensor in ANGLE mode
gy.mode='GYRO-ANG'
us.mode='US-DIST-CM'

units = gy.units

while True:
	lcd.clear()
	angle = gy.value() % 360
	distance = us.value()/10
	lcd.draw.text((30,60), str(angle) + " " + units, font=dispFont)
	lcd.draw.text((30,30), str(distance) + " cm", font=dispFont)
	print("Current angle:", angle, "Current distance:", distance)
	lcd.update()
	sleep(0.5)

