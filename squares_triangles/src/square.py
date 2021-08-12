from nose.tools import *
import numpy as np

from utils.fractals import Fractals

def squares():
    Squares = Fractals(4, 'squares', 5)
    Squares.set_up_plot()

    #square
    print('Making first square')
    first_shape = [[0.5,0.5],
                      [0.5,-0.5],
                      [-0.5,-0.5],
                      [-0.5,0.5]]

    Squares.make_the_image(first_shape)



if __name__ == '__main__':
    squares()