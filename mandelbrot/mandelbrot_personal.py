# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:06:06 2017

@author: DUDFI00P
"""

import cmath
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
import PIL.Image as Image
from PIL import ImageFont
from PIL import ImageDraw

from mandelbrot import mandelbrot_zoom, plot_sub


z= complex(-1,0)

ylim = [-2,2]
xlim = [-2.25,1.75]

ylim = [-2,2]
xlim = [-2.5,1.5]

N=512
NN = 100

dx = xlim[1]/N-xlim[0]/N
dy = ylim[1]/N-ylim[0]/N

xlist =[]
ylist = []

s = '1988-10-02'
seed = 1
for letter in s:
    seed = seed*ord(letter) % 2**32

np.random.seed(seed)

r = np.random.uniform(0,5)
print(r,seed)

now = datetime.now().strftime("_%Y-%m-%d_%H_%M_%S")

img = mandelbrot_zoom(xlim=xlim,ylim=ylim,N=N,s=s,NN=NN)

# img = Image.fromarray(256-logic_map*256/NN)
# img.show()
img = img.convert('RGB')

draw = ImageDraw.Draw(img)
font_path = "/Users/admin/Library/Fonts/InputSans-Regular.ttf"
# font = ImageFont.truetype(font_path, 20)
draw.text((230, 50),s,(0,0,0))

img.save("Images/" + s + "_mandelbrot_"+str(N)+"_"+now + ".png")

         
    