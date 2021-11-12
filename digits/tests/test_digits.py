# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:27:32 2018

@author: DUDFI00P
"""
import matplotlib.pyplot as plt
from digits.src.digits import Digits


def test_letter():
    letters = ["a", "c", "d", "e", "f", "g", "i", "l", "o", ["phi"], "p", "r"]
    for letter in letters:
        d = Digits(letter)
        d.plot_digits(add_text=1, add_mart=1, add_equation=1, add_description=1, save_fig=True)


def test_digits_phi():
    d = Digits(["phi"], cols=16, rows=20)
    d.plot_digits(add_mart=1)
    d.plot_digits(add_text=1, add_mart=1)


def test_digits_e_phi():
    d = Digits("e", cols=16, rows=20)
    d.plot_digits(add_mart=1)
    d.plot_digits(add_text=1, add_mart=1)


def test_digits_p_phi():
    d = Digits("p", cols=16, rows=20)
    d.plot_digits(add_mart=1)
    d.plot_digits(add_text=1, add_mart=1)
