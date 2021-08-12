# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:06:06 2017

@author: DUDFI00P
"""

import cmath
import numpy as np 

import matplotlib.pyplot as plt
import PIL.Image as Image

from contours import mask_to_coord, coord_to_mask

import cv2

z= complex(-1,0)

ylim = [-2,2]
xlim = [-2.25,1.75]

ylim = [-2,2]
xlim = [-2.5,1.5]

N=512*4
NN = 100

dx = xlim[1]/N-xlim[0]/N
dy = ylim[1]/N-ylim[0]/N

xlist =[]
ylist = []



def f(z,c):
    
    y = z**2+c
    return y

logic_map = np.zeros((N,N))
for i in range(0,N):
    for j in range(0,int(N/2)):
        
        x = xlim[0]+i*dx
        y = ylim[0]+j*dy
        c = complex(x,y)
        z = f(0,c)
        
        k=0
        k_save=0
        while k<NN:
            z = f(z,c)
            k_save = k
            if cmath.polar(z)[0]>10:
                k=NN
            k=k+1
            
        #if cmath.polar(z)[0]<10:
        logic_map[i,j]=k_save
        logic_map[i,N-j-1]=k_save
            
        
        if (i*N + j)/N/N*100 % 1==0:
            print(str((i*N + j)/N/N*100) + '%',end='\r')
            
#heatmap = plt.pcolor(logic_map)
#plt.colorbar(heatmap)
logic_map_unit = logic_map.astype('uint8')
logic_map_unit[logic_map<99]=0
logic_map_unit[logic_map>=99]=99

#filter out disjointed pixes
c = mask_to_coord(logic_map_unit.astype('uint8'),99,threshold_area=100,smooth_len=2)
mask = coord_to_mask(c,logic_map_unit.shape)

#save
img = Image.fromarray(256-mask)
img.show()
img = img.convert('RGB')
img.save("Images/mandelbrot_"+str(N)+"svg.png")



         
    