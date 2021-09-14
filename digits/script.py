# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:27:32 2018

@author: DUDFI00P
"""
import matplotlib.pyplot as plt
from utils.digits import Digits

letters = ["a", "c", "d", "e", "f", "g", "i", "l", "o", ["phi"], "p", "r"]
for letter in letters:
    fig = plt.figure(figsize=(10, 10))
    d = Digits(letter)
    # d.plot_digits(add_mart=1)
    # d.plot_digits(add_text=1,add_mart=1)
    # d.plot_digits(add_text=1,add_mart=1,save_fig=True)
    d.plot_digits(add_text=1, add_mart=1, add_equation=1, add_description=1, save_fig=True)


d = Digits(["phi"], cols=16, rows=20)
d.plot_digits(add_mart=1)
d.plot_digits(add_text=1, add_mart=1)

d = Digits("e", cols=16, rows=20)
d.plot_digits(add_mart=1)
d.plot_digits(add_text=1, add_mart=1)

fig = plt.figure(figsize=(7, 10))
d = Digits("p", cols=16, rows=20)
d.plot_digits(add_mart=1)
d.plot_digits(add_text=1, add_mart=1)
