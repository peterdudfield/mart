import cmath, random
import numpy as np

import matplotlib.pyplot as plt
import PIL.Image as Image

def f(z, c, r):
    y = (z ** (2 + r) + c)
    return y


def mandelbrot_zoom(xlim, ylim, sub_plot_idx=0, N=500, s=None, NN=100):
    """

    :param xlim:
    :param ylim:
    :param i:
    :param N:
    :param s:
    :return:
    """

    if s is not None:
        str_start = int((sub_plot_idx / 4) * len(s))
        str_end = int((sub_plot_idx + 1) * len(s) / 4)

        seed = 1
        sub_str = s[str_start:str_end]
        print(sub_str)
        for letter in sub_str:
            seed = seed * ord(letter) % 2 ** 32

        np.random.seed(seed)
        r = np.random.uniform(0, 4)
        # print(r)
    else:
        r = 0
        # print(r)

    if sub_plot_idx == 2:
        for j in [0, 1]:
            xlim[j] += r / 10

    # if i==1:
    #     for j in [0,1]:
    #         ylim[j] += r/10

    dx = xlim[1] / N - xlim[0] / N
    dy = ylim[1] / N - ylim[0] / N

    logic_map = np.zeros((N, N))
    for i in range(0, N):
        for j in range(0, N):

            x = xlim[0] + i * dx
            y = ylim[0] + j * dy
            c = complex(x, y)
            z = f(0, c, r)

            k = 0
            k_save = 0
            while k < NN:
                k_save = k
                if cmath.polar(z)[0] > 2:
                    k = NN
                k = k + 1
                z = f(z, c, r)

            # if cmath.polar(z)[0]<10:
            # logic_map[i,j]=int(k_save^(int(r))) / (NN^(int(r)))
            logic_map[i, j] = k_save
            # logic_map[i,N-j-1]=k_save

            if (i * N + j) / N / N * 100 % 1 == 0:
                print(str((i * N + j) / N / N * 100) + '%', end='\r')

    img = Image.fromarray(256 - logic_map * 256 / (NN-1))

    return img


def rotate_flip(img, rotate=0, flip_v=False,flip_h=False):

    # print('Rotate: ' + str(rotate))
    # print('flip_v: ' + str(flip_v))
    # print('flip_h: ' + str(flip_h))

    # if rotate != 0:
    #     img = img.rotate(rotate)

    if flip_v:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

    if flip_h:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    return img


def plot_sub(img, n, fig, rotate=0, flip_v=False,flip_h=False):

    ax = fig.add_subplot(220 + n)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])

    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')