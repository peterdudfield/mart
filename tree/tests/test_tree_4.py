import matplotlib.pyplot as plt
import numpy as np

from tree.src.tree_4 import make_tree

min_N_layers = 6


def test_plot_1():
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(220 + 1)
    print("Making tree 1")
    make_tree(np.pi / 3 * 0.8, np.pi / 3 * 0.9, 0.3, 0.2, 1.4, N_layers=min_N_layers + 1, ax=ax)
