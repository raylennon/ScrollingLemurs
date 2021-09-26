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
for line in lines[5:]:

    image = Image.open('lemur-photos/'+random.choice(os.listdir("lemur-photos/")))
    img_width, img_height = image.size

    xpos=-2
    while xpos<=img_width-64:
        xpos += 1
        offscreen_canvas.SetImage(image, -xpos)
        offscreen_canvas.SetImage(image, -xpos + img_width)

        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep(0.03)


    lemur = line.split(",")[0]
    status = line.split(",")[1]
    names = line.split(",")[2:]
    
    namestr = f"The Duke Lemur Center has {len(names)} {lemur}s! Their names are "
    for i in range(len(names)-1):
        namestr+= name
        namestr+= ", "
    namestr += "and "
    namestr += names[-1]
    namestr += "."
    

    pos = offscreen_canvas.width

    length = 0 # overkill? lol

    #print(pos+length)
    while (pos + length > 0):

        offscreen_canvas.Clear()
        length = graphics.DrawText(offscreen_canvas, font, pos, 15, textColor, lemur)
        pos -= 1

        time.sleep(0.03)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
    
    if len(names):
        length=0
        while (pos + length + > 0):

            offscreen_canvas.Clear()
            length = graphics.DrawText(offscreen_canvas, font, pos, 15, textColor, namestr)
            pos -= 1

            time.sleep(0.03)
            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)

    matrix.Clear()
