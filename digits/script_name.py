# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:27:32 2018

@author: DUDFI00P
"""
import matplotlib.pyplot as plt

from circle.src.digits import Digits

name = "peter"


add_equation = True
add_description = True

fig = plt.figure(figsize=(len(name) * 10, 10))

d = Digits(name)

for i in range(0, len(name)):

    if i < len(name) - 1:
        d.plot_digits(
            fig=fig,
            add_text=0,
            add_equation=add_equation,
            add_description=add_description,
            N_letters=len(name),
            current_letter=i,
        )
    else:

        d.plot_digits(
            add_text=1,
            add_equation=add_equation,
            add_description=add_description,
            N_letters=len(name),
            current_letter=i,
            add_mart=True,
            save_fig=True,
            # filename='images/' +name+ '.png',
        )
