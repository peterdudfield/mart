from nose.tools import *
import numpy as np

from utils.fractals import Fractals


def triangles():
    Triangles = Fractals(3, "triangles", 5)
    Triangles.set_up_plot()

    # square
    first_shape = [
        [np.cos(0), np.sin(0)],
        [np.cos(np.pi * 2 / 3), np.sin(np.pi * 2 / 3)],
        [np.cos(np.pi * 2 / 3), np.sin(np.pi * 4 / 3)],
    ]

    Triangles.make_the_image(first_shape)


if __name__ == "__main__":
    triangles()
