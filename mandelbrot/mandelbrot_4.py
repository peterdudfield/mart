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

from datetime import datetime

z = complex(-1, 0)

ylim = [-2, 2]
xlim = [-2.25, 1.75]

ylim = [0, 0.3]
xlim = [-0.9, -0.6]

N = 1000
NN = 100

fig = plt.figure(figsize=(10, 10))

print("figure 1")
img1 = mandelbrot_zoom([-2.5, 1.5], [-2, 2], N=N, NN=NN)
plot_sub(img1, 1, fig)

print("figure 2")
img2 = mandelbrot_zoom([-0.9, -0.6], [0, 0.3], N=N, NN=NN)
plot_sub(img2, 2, fig)

print("figure 3")
img3 = mandelbrot_zoom([-0.0, 0.6], [-0.3, 0.3], N=N, NN=NN)
plot_sub(img3, 3, fig)

print("figure 4")
img4 = mandelbrot_zoom([-0.4, 0.2], [0.6, 1.2], N=N, NN=NN)
plot_sub(img4, 4, fig)

now = datetime.now().strftime("_%Y-%m-%d_%H_%M_%S")

plt.tight_layout(pad=5, w_pad=5, h_pad=5)
plt.savefig("mandelbrot_4_" + str(N) + "_" + now + "_.png", dpi=250)
# img = img.convert('RGB'0
# img.save("mandelbrot_zoom_"+str(N)+".png")
