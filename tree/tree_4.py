# import matplotlib as mpl
# mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from tree.src.tree_4 import make_tree

min_N_layers = 6

# set up plot
fig = plt.figure(figsize=(15, 15))
# fig,ax = plt.subplots(1)
# ax=plt.axes()
# ax.set_aspect('equal')

ax = fig.add_subplot(220 + 1)
print("Making tree 1")
make_tree(np.pi / 3 * 0.8, np.pi / 3 * 0.9, 0.3, 0.2, 1.4, N_layers=min_N_layers + 1, ax=ax)

ax = fig.add_subplot(220 + 2)
print("Making tree 2")
make_tree(np.pi / 3 * 0.8, np.pi / 3 * 0.8, 0.7, 0.7, 2, scalefactor=1.6, N_layers=min_N_layers + 3, ax=ax)

ax = fig.add_subplot(220 + 3)
print("Making tree 3")
make_tree(
    np.pi / 4 * 0.8, np.pi / 3 * 1.2, 0.5, 0.5, 1.5, scalefactor=1.9, N_layers=min_N_layers + 1, ax=ax
)

ax = fig.add_subplot(220 + 4)
print("Making tree 4")
make_tree(np.pi / 4 * 1.2, np.pi / 4 * 1.1, 0.4, 0.8, 1.5, N_layers=min_N_layers + 1, ax=ax)

plt.tight_layout(pad=5, w_pad=5, h_pad=5)

plt.savefig("Images/tree_4.png", dpi=250)
