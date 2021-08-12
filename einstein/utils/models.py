"""

"""

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
#from keras.preprocessing import sequence

def get_nn(N_distinct_words):
    

    model = Sequential()
    model.add(Dense(256, input_dim=10,activation='relu'))
    #model.add(Dense(128, input_dim=10,activation='relu'))
    model.add(Dense(256 ,activation='relu'))
    model.add(Dense(N_distinct_words,activation='softmax'))
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              )
    
    return model

def get_LSTM(N_distinct_words):
    
    embedding_vecor_length=32
    model = Sequential()
    model.add(Embedding(N_distinct_words, embedding_vecor_length, input_length=10))
    model.add(LSTM(100))
    model.add(Dense(N_distinct_words,activation='softmax'))
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              )
    
    return model