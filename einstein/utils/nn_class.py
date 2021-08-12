# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:04:21 2018

Markov change on einsteins 1905

@author: DUDFI00P
"""

import numpy as np
from utils.latex import read_tex, make_tex
from utils.models import get_nn, get_LSTM
from utils.data import data_generator


class Word_prediction_nn():
    def __init__(self,batch_size=32,tex_file='1905_tex.tex',verbose=False):
        
        self.batch_size = batch_size
        self.tex_file = tex_file
        
        if verbose:
            print('load text')
        text_str = read_tex(tex_file,rm_last_rows=5,rm_first_rows=20)
        word_list = text_str.split(' ')[1:-1]
        
        self.word_list = word_list
        
        self.N_words = len(word_list)
        print('Found ' + str(self.N_words) + ' words')
        
        if verbose:
            print('Make list of words')
            
        self.words_distinct_list = []
        for word in word_list:
            if word not in self.words_distinct_list:
                self.words_distinct_list.append(word)
                
                
            #make words index
            self.index_to_words = {ix:word for ix, word in enumerate(self.words_distinct_list)}
            self.words_to_index = {word:ix for ix, word in enumerate(self.words_distinct_list)}

        
        self.N_distinct_words = len(self.words_distinct_list)
        print(self.words_distinct_list[0:20])
        print('Found ' + str(self.N_distinct_words) + ' different words')

        #get list of number for words
        self.word_list_idx = [self.words_to_index[word] for idx, word in enumerate(self.word_list)]
        
        #set up data generator        
        self.train_genetor = data_generator(self.word_list_idx,self.N_distinct_words)
        
    def set_up_nn(self,model_name = 'NN'):
        
        self.model_name = model_name
        
        if model_name == 'NN':
            self.model = get_nn(self.N_distinct_words)
        if model_name == 'LSTM':
            self.model = get_LSTM(self.N_distinct_words)
            
    def check_data_generator(self):

        #check train_genetor is working
        x,y = next(self.train_genetor)
        x_str = ''
        for x1 in x[0]:
            x_str = x_str + self.index_to_words[x1] + ' '
        print('Check train genetor is working')
        print('Input: ', x_str)
        print('Output:',self.index_to_words[np.where(y[0]==1)[0][0]])
        
    def train(self,N_epochs=100):
        
        self.N_epochs = N_epochs
        
        #train
        self.model.fit_generator(self.train_genetor,
                    steps_per_epoch=self.N_words // self.batch_size,
                    epochs=N_epochs)
        
    def predict(self,N_predictions=1000):
        
        #predict
        initial_state = np.array(self.word_list_idx[0:10])
        predict_words = []
        for word_idx in initial_state:
            predict_words.append(self.index_to_words[word_idx])
    
        currnet_state = initial_state
    
        for i in range(0,N_predictions):
    
            r = np.random.random(1)[0]
    
            probs = self.model.predict(np.expand_dims(currnet_state,axis=0))[0]
            probs = np.cumsum(probs)
    
            if probs[0]>r:
                next_state=0
            else:
                next_state = np.where(np.all([probs[:-1]<=r,probs[1:]>r],axis=0))[0][0]+1
    
            next_word = self.index_to_words[next_state]
            if next_word in ['.', '\n','\\section{','\\subsection{']:
                next_word = next_word[0].upper() + next_word[1:]
        
            predict_words.append(self.index_to_words[next_state])
    
            #update for next prediction
            currnet_state[0:9] = currnet_state[1:]
            currnet_state[9] = next_state
  
        self.predict_words = predict_words
    
        predict_str = ''
        for word in self.predict_words:
            predict_str = predict_str + word + ' '
        
        self.predict_str = predict_str
        
    def save(self,verbose=False):
        
        if verbose:
            print(self.predict_str)   
        make_tex(self.predict_str,self.model_name)


