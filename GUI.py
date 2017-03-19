#!/usr/bin/python

from tkinter import *
import time
import math

root=Tk()
root.title("Radar")

windowFrameThickness = 10

windowHeight = 800 + windowFrameThickness*2
windowWidth = windowHeight
radarRadius = 400

centre = [windowHeight/2, windowWidth/2]

canvas = Canvas(root,
		width=windowWidth,
		height=windowHeight)

canvas.pack()

canvas.create_oval(centre[0] - radarRadius,
		   centre[1] - radarRadius,
		   centre[0] + radarRadius,
		   centre[1] + radarRadius,
		   width = 5)


#Build dataset list to put US data into based on angle
USdata = []
for x in range(1,360):
	USdata.extend([0])

USdata





iterator = 0
while True:
	root.update_idletasks()
	root.update()

	x = centre[0] + radarRadius*math.cos(iterator)
	y = centre[1] + radarRadius*math.sin(iterator)

	canvas.create_line(centre[0], centre[1], x, y, width = 2)
	iterator = iterator + 1

	time.sleep(0.1)


