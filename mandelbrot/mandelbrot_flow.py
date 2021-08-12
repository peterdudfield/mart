# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:06:06 2017

@author: DUDFI00P
"""

import cmath
import numpy as np 

import matplotlib.pyplot as plt
import PIL.Image as Image
import itertools
import os

import datetime

from src.mandelbrot import mandelbrot_zoom, plot_sub



z= complex(-1,0)

ylim = [-2,2]
xlim = [-2.25,1.75]

ylim = [0,0.3]
xlim = [-0.9,-0.6]

N=500
if os.path.exists("Images/"+str(N))==False:
    os.mkdir("Images/"+str(N))
NN = 100
    
M=7
N_possible_permuations = int(M*(M-1)*(M-2)/6)
t=itertools.permutations( np.array(range(M)))

now = datetime.datetime.now()


N_plots=0
plot_dict={}
while N_plots<N_possible_permuations:
    r= sorted(next(t)[0:4])

    name=str(r[0])+str(r[1])+str(r[2])+str(r[3])
    
    if name not in plot_dict.keys():
        
        fig = plt.figure(figsize=(10,10))
    
        for i in range(4):
    
            y=2**r[i]
            img = mandelbrot_zoom([-2.1, 2.1],[-2.1, 2.1],NN=y+1)
            plot_sub(img,i+1,fig)
            
        plt.text(N/2,N*1.1,r'$\mathcal{M} \alpha r \tau$ '+str(N_plots+1)+'/'+str(N_possible_permuations)+' ' + now.strftime("%Y-%m-%d"))
       
        plt.tight_layout(pad=5, w_pad=5, h_pad=5)    
        plt.savefig("Images/"+str(N)+"/mandelbrot"+'_2x2_'+name+".png",dpi=250)
        
        plot_dict[name]=True
        
        print(name + ': '+str(N_plots) + '/' + str(N_possible_permuations))
        
        N_plots+=1
    
#plt.tight_layout(pad=5, w_pad=5, h_pad=5)    
#pl.t.savefig("mandelbrot_4_"+str(N)+".png",dpi=250)
#img = img.convert('RGB')
#img.save("mandelbrot_zoom_"+str(N)+".png")

         
    