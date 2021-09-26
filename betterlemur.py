#!/usr/bin/env python
# Display a runtext with double-buffering.
from PIL import Image
import random

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from rgbmatrix import graphics
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time


#import getlemurdata

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
font.LoadFont("fonts/7x13.bdf")

textColor = graphics.Color(255, 255, 0)
pos = offscreen_canvas.width

file = open('/home/pi/ScrollingLemurs/endangered.txt', 'r')
lines = file.readlines()


out = []
for line in lines:
    lemur = line.split(",")[0]
    print(lemur)

    status = line.split(",")[1]

    pos = offscreen_canvas.width

    length = -100 # overkill? lol
    print(pos+length)
    while True:

        offscreen_canvas.Clear()
        length = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, lemur)
        pos -= 1

        if (pos + len < 0):
            pos = offscreen_canvas.width

        print(pos+length)
        time.sleep(0.05)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
    
    matrix.Clear()
