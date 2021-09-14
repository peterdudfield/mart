# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:06:06 2017

@author: DUDFI00P
"""

import cmath
import numpy as np

import matplotlib.pyplot as plt
import PIL.Image as Image

from src.mandelbrot import mandelbrot_zoom, plot_sub

z = complex(-1, 0)

ylim = [-2, 2]
xlim = [-2.25, 1.75]

ylim = [-2, 2]
xlim = [-2.5, 1.5]

N = 512
NN = 100

dx = xlim[1] / N - xlim[0] / N
dy = ylim[1] / N - ylim[0] / N

xlist = []
ylist = []


img = mandelbrot_zoom(xlim=xlim, ylim=ylim, N=N, NN=NN)

img.show()
img = img.convert("RGB")
img.save("Images/mandelbrot_" + str(N) + ".png")
