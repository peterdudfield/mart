# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:01:48 2017

Creat random tree

@author: peter
"""

import numpy as np
import matplotlib.pyplot as plt

N=100
dx=1/N

#define probability
def prob_split(distance_from_last_split):
    
    p = distance_from_last_split
    
    return p

#first splits
points = []
points.append(0)
n_splits=0
r = np.random.rand(N)
for i in range(0,N):
    
    x=i*dx
    if r[i]<prob_split(x-points[-1]):
        points.append(x)
        
        n_splits+=1
        
average_length_between_splits = np.mean(np.array(points)[1:] - np.array(points)[0:-1])

#second split
length = []
total_length = []
second_points = []
for i in range(0,len(points)):
    length.append(np.random.beta(2,2)*(1-points[i]))
    
    
    x = points[i]
    if i%2 ==0:
        y=length[i]
    else:
        y=-length[i]
    
    
    second_points.append([x,0,x,length[i]])
    second_points.append([x,0,x,-length[i]])
    total_length.append(points[i] + length[-1])
    total_length.append(points[i] + length[-1])

def plot_points(points,color):
    for i in range(len(points)):
        plt.plot([points[i][1],points[i][3]],[points[i][0],points[i][2]],color)    
    
def make_lines(second_points,total_length_old):    
    #third split
    length = []
    third_points = []
    total_length_old = []
    for i in range(0,len(second_points)):
        length.append(np.random.beta(2,2)*(1-total_length[i]))
        #total_length[i] += length[-1]
    

        s1 = np.sign(second_points[i][2]-second_points[i][0])
        s2 = np.sign(second_points[i][3]-second_points[i][1])
        print(s1,s2)
    
        if s1==0 or s1<0:
            third_points.append([second_points[i][2],
                             second_points[i][3],
                             second_points[i][2]-length[-1],
                             second_points[i][3]])
        if s1==0 or s1>0:
            third_points.append([second_points[i][2],
                             second_points[i][3],
                             second_points[i][2]+length[-1],
                             second_points[i][3]])
        if s2==0 or s2<0:
            third_points.append([second_points[i][2],
                             second_points[i][3],
                             second_points[i][2],
                             second_points[i][3]+length[-1]])
        if s2==0 or s2>0:
            third_points.append([second_points[i][2],
                             second_points[i][3],
                             second_points[i][2],
                             second_points[i][3]-length[-1]])
    
        total_length_old.append(total_length[i]+length[i])
        total_length_old.append(total_length[i]+length[i])
        total_length_old.append(total_length[i]+length[i])
    
    return third_points, total_length_old

third_points, total_length = make_lines(second_points,total_length)
fourth_points, total_length = make_lines(third_points, total_length) 
    
fig = plt.figure()
plt.plot([0,0],[-0.2,1],'r')
   
plot_points(second_points,'b')   
plot_points(third_points,'g')   
plot_points(fourth_points,'r')   
   


