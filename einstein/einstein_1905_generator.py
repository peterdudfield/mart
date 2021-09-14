# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:04:21 2018

Markov change on einsteins 1905

@author: DUDFI00P
"""

from utils.einstein_1905_class import Word_prediction_nn

wpn = Word_prediction_nn()
wpn.set_up_markov()
wpn.predict(prediction_method="weighted_random")
wpn.save()


wpn = Word_prediction_nn()
wpn.set_up_nn("NN")
wpn.check_data_generator()
wpn.train()
wpn.predict()
wpn.save()

wpn = Word_prediction_nn()
wpn.set_up_nn("LSTM")
wpn.check_data_generator()
wpn.train()
wpn.predict(prediction_method="weighted_random")
wpn.save()
