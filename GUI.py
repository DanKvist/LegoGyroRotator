#!/usr/bin/python

import TKinter as tk


app = radarWindow(None)
app.title('SYSTEM CONTROL')


class radarWindow(Tkinter.Tk):
	def __init__(self,parent):
		TKinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		pass
