# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:06:06 2017

@author: DUDFI00P
"""

import random, argparse, time, csv
import matplotlib.pyplot as plt
import numpy as np

from src.mandelbrot import mandelbrot_zoom, plot_sub, rotate_flip
from src.plot_utils import watermark_text, watermark_with_transparency
from datetime import datetime

z= complex(-1,0)

ylim = [-2,2]
xlim = [-2.25,1.75]

ylim = [0,0.3]
xlim = [-0.9,-0.6]

N=1000 #number of pixels across
NN = 100


# def get_arguments():
#     parser = argparse.ArgumentParser(description='Optimizer package, used to optimize a battery')
#
#     parser.add_argument(
#         '--s',
#         help='The title of the art work, the random number is generated from this string',
#         default='Personal Artwork')
#
#     args = parser.parse_args()
#
#     return args


def get_names():
    names = []

    with open('data/names.txt', 'r') as f:

        rows = f.read().split(',\n')
        print(rows)
        for row in rows:
            names.append(row)
            print(row)

    return names

names = get_names()

for name in names:

    s = name
    print(s)

# args = get_arguments()
# s = args.s

    orginial_s = s
    seed = 1
    for letter in s:
        seed = seed * ord(letter) % 2 ** 32

    random.seed(seed)
    np.random.seed(seed)
    s = ''.join(random.sample(s,len(s)))

    order = np.random.permutation([0,1,2,3])
    rotates = np.random.randint(0,360,4)
    flip_hs = np.random.randint(0, 2, 4)
    flip_vs = np.random.randint(0, 2, 4)

    fig = plt.figure(figsize=(10,10))

    xlims = [[[-2.5, 1.5],[-2, 2]],
             [[-0.9, -0.3],[0.1, 0.6]],
             [[-0.0, 0.6],[-0.3, 0.3]],
             [[-0.4, 0.2],[0.6, 1.2]]]

    for i in range(0,4):
        print('figure ' + str(i))
        img1 = mandelbrot_zoom(xlims[i][0], xlims[i][1], i, N=N, s=s, NN=NN)
        img1 = rotate_flip(img1, rotates[i], flip_hs[i], flip_vs[i])
        plot_sub(img1, order[i] + 1, fig)


    now = datetime.now().strftime("_%Y-%m-%d_%H_%M_%S")
    'Personal Art Work_mandelbrot_4_500__2019-02-23_11_58_31_'

    plt.tight_layout(pad=5, w_pad=5, h_pad=5)
    orginial_s = orginial_s.replace('/','__')

    filename = "Images/Personal/"+orginial_s+"_mandelbrot_4_"+str(N)+".png"
    filename_preview = filename.replace('.png', '_preview.png')

    ax = plt.subplot(224)
    plt.savefig(filename, dpi=250)

    plt.text(N / 3, N * 1.1, r'$\mathcal{M} \alpha r \tau$ ' + datetime.now().strftime(" %Y-%m-%d"))
    fig.suptitle(orginial_s)
    plt.savefig(filename_preview, dpi=250)
    watermark_with_transparency(filename_preview, filename_preview, 'Images/preview/preview.png', position=(300, 300))
    #img = img.convert('RGB'0

    plt.close()
    #img.save("mandelbrot_zoom_"+str(N)+".png")

         
    