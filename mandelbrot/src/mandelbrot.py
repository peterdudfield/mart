import cmath, random
import numpy as np

import matplotlib.pyplot as plt
import PIL.Image as Image

from typing import List, Optional


def f(z: complex, c: complex, r: float = 0) -> complex:
    """
    Mandelbrot iterative function

    :param z: Complex number
    :param c: constant parameters, typically 0 on the first iteration
    :param r: extra number that is added to the squared term. This is used to make weird and wonderful
    quasi mandelbrot sets. r=0, is the classic mandelbrot set
    :return: complex number
    """
    y = z ** (2 + r) + c
    return y


def mandelbrot_zoom(
    xlim: List[int],
    ylim: List[int],
    sub_plot_idx: int = 0,
    N: int = 500,
    s: Optional[str] = None,
    NN: int = 100,
) -> Image:
    """
    Create a Mandelbrot image

    There are options to zoom into a certain area, if you like.

    :param xlim: The x coordinate limit.
    :param ylim: The y coordinate limit
    :param NN: The number of the mandlebrot function is iterated.
    :param N: The number of pixels to make in the image. Typically 512 is good for a4 printing
    :param s: Optional string to create a random seed from. The random seed also uses sub_plot_idx which sub plot this is

    :return: PIL Image
    """

    if s is not None:
        # create a random seed, which is used to manipulate the mandlebrot set.

        # get sub string, depending on what sub plot it is
        str_start = int((sub_plot_idx / 4) * len(s))
        str_end = int((sub_plot_idx + 1) * len(s) / 4)

        # start with seed 1, but then types this by the 'ord' of the letter in the sub-string
        seed = 1
        sub_str = s[str_start:str_end]
        print(sub_str)
        for letter in sub_str:
            seed = seed * ord(letter) % 2 ** 32

        # make random seed
        np.random.seed(seed)
        r = np.random.uniform(0, 4)
    else:
        # r=0, means the classic mandelbrot set
        r = 0

    if sub_plot_idx == 2:
        for j in [0, 1]:
            xlim[j] += r / 10

    # create the deltas in the x and y cooridantes
    dx = xlim[1] / N - xlim[0] / N
    dy = ylim[1] / N - ylim[0] / N

    # define the NxN space, which says if the pixel is in the set or not
    logic_map = np.zeros((N, N))

    # loop over pixels
    for i in range(0, N):
        for j in range(0, N):

            # create x and y for this pixel and run first iteration
            x = xlim[0] + i * dx
            y = ylim[0] + j * dy
            c = complex(x, y)
            z = f(0, c, r)

            # keep iterating using over the mandelbrot equation and see if the grows greater than 2.
            k = 0
            k_save = 0
            while k < NN:
                k_save = k
                if cmath.polar(z)[0] > 2:
                    k = NN
                k = k + 1
                z = f(z, c, r)

            # save after how many iterations the number is not in the set.
            # This is useful for creating some shading on the image
            logic_map[i, j] = k_save

            if (i * N + j) / N / N * 100 % 1 == 0:
                print(str((i * N + j) / N / N * 100) + "%", end="\r")

    img = Image.fromarray(256 - logic_map * 256 / (NN - 1))

    return img


def rotate_flip(img, rotate=0, flip_v=False, flip_h=False):

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


def plot_sub(img, n, fig, rotate=0, flip_v=False, flip_h=False):

    ax = fig.add_subplot(220 + n)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])

    ax.spines["bottom"].set_color("white")
    ax.spines["top"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["right"].set_color("white")
