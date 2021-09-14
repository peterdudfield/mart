# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:06:06 2017

@author: DUDFI00P
"""

import cmath
import numpy as np
import cv2
import os

import matplotlib.pyplot as plt
import PIL.Image as Image

from src.mandelbrot import mandelbrot_zoom, plot_sub

z = complex(-1, 0)

ylim = np.array([-2, 2])
xlim = np.array([-2.5, 1.5])

N = 512
NN = 100

r = 0.95

dx = xlim[1] / N - xlim[0] / N
dy = ylim[1] / N - ylim[0] / N

M = [-1.401155189, 0]

xlist = []
ylist = []

images = []

for i in range(0, 75):

    print("*****")
    print(i)
    print("*****")

    NN = NN + i * 0.25
    ylim = ylim * r + (1 - r) * M[1]
    xlim = xlim * r + (1 - r) * M[0]

    if i > 150:

        img = mandelbrot_zoom(xlim=xlim, ylim=ylim, N=N, NN=NN)

        img = img.convert("RGB")

        if i < 10:
            s = "0" + str(i)
        else:
            s = str(i)

        img.save("Images/Video/mandelbrot_" + s + "_" + str(N) + ".png")

        images.append(img)


image_folder = "Images/Video"
video_name = "Images/Video/video.avi"

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images = sorted(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

for i in range(0, 10):
    for image in images[29:]:
        video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
