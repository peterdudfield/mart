# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:06:33 2018

@author: DUDFI00P
"""

import csv
import numpy as np

#create data generator
def data_generator(word_list_idx,N_distinct_words,batch_size=32):
    
    while True:
        
        r = np.random.randint(0,N_distinct_words-batch_size-1)
        
        x_batch = []
        y_batch = []
        for i in range(0,batch_size):
        
            x = word_list_idx[r:r+10]
            y = np.zeros((N_distinct_words,))
            y[word_list_idx[r+10]]=1
            
            x_batch.append(x)
            y_batch.append(y)
    
        x_batch = np.array(x_batch) 
        y_batch = np.array(y_batch) 

        yield x_batch,y_batch
    
    