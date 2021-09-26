#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from PIL import Image
import random

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from rgbmatrix import graphics
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time


import getlemurdata

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.gpio_slowdown = 2
options.brightness=20
options.hardware_mapping = 'adafruit-hat'
options.daemon = False
options.drop_privileges = False
matrix = RGBMatrix(options = options)


offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("7x13.bdf")

textColor = graphics.Color(255, 255, 0)
pos = offscreen_canvas.width

file = open('/home/pi/ScrollingLemurs/endangered.txt', 'r')
lines = file.readlines()


out = []
for line in lines:
    lemur = line.split(",")[0]
    status = line.split(",")[1]

    pos = offscreen_canvas.width

    length = 1e99 # overkill? lol

    while (pos + length < 0):

        offscreen_canvas.Clear()
        length = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, lemur)
        pos -= 1

        time.sleep(0.05)
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas
    
    matrix.clear()















class Lemur(SampleBase):
	def __init__(self, *args, **kwargs):        
		super(Lemur, self).__init__(*args, **kwargs)

		file = open('/home/pi/ScrollingLemurs/endangered.txt', 'r')
		lines = file.readlines()

		out = []
		for line in lines:
			out.append(line.split(',')[0])
			print(line.split(',')[1])
			out.append(line.split(',')[1])
			if len(line.split(','))>2:
				names = line.split(',')[2].split('/')
				out[-2]+="  ...  the Duke Lemur Center has "+ str(len(names))+" of this species! Their names are: "
				out[-2]+=', '.join(names[0:-1])
				out[-2]+=(', and '+names[-1][0:-1]+'. Their status is ')
		files=['wide-lemur.ppm', 'wide-mouse-lemur.ppm']
		filename=files[random.randint(0,1)]

		self.parser.add_argument("-t", "--text", help="The text array to scroll on the RGB LED panel", default=out)
		self.parser.add_argument("-i", "--image", help="The image to display", default="/home/pi/rpi-rgb-led-matrix/examples-api-use/lemur-photos/"+filename)


	def run(self):

		offscreen_canvas = self.matrix.CreateFrameCanvas()
		font = graphics.Font()
		font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")
		textColor = graphics.Color(0, 100, 255)
		textColor2 = graphics.Color(255, 255, 0)

		pos = offscreen_canvas.width
		data = self.args.text

		index=0
		length=0
		files=['wide-lemur.ppm', 'wide-mouse-lemur.ppm', 'wide-loris.ppm']

		while True:
			filename=files[random.randint(0,len(files)-1)]
			self.image = Image.open("/home/pi/ScrollingLemurs/lemur-photos/"+\
				random.choice(os.listdir("/home/pi/ScrollingLemurs/lemur-photos/")))
	
			img_width, img_height = self.image.size

			# let's scroll
			xpos=-2
			while xpos<=img_width-64:
				xpos += 1
				offscreen_canvas.SetImage(self.image, -xpos)
				offscreen_canvas.SetImage(self.image, -xpos + img_width)

				offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
				time.sleep(0.03)


			if index==len(data):
				index=0;

			pos = offscreen_canvas.width
			data = self.args.text
			length=0
			data[index+1]=data[index+1][0:-1]


			if data[index+1]=='Endangered':
				textColor2 = graphics.Color(255,165,0)
			elif data[index+1]=='Vulnerable':
				textColor2 = graphics.Color(255,255,0)
			elif data[index+1]=='Data Deficient':
				textColor2 = graphics.Color(255,255,255)
			elif data[index+1]=='Critically Endangered':
				textColor2 = graphics.Color(255,0,0)
			elif data[index+1]=='Least Concern':
				textColor2=graphics.Color(0,255,0)
			else:
				textColor2 = graphics.Color(255, 0, 255)


			for i in range(len(data[index]+": "+data[index+1]+"  ")*8+100):
				offscreen_canvas.Clear()
				length = graphics.DrawText(offscreen_canvas, font, pos, 16, textColor, data[index]+": ")+\
					graphics.DrawText(offscreen_canvas, font, pos+len(data[index])*8, 16, textColor2, data[index+1])
				pos -= 1
				time.sleep(0.03)
				offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
			index+=2