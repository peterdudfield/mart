from paper.src.utils import Dragon
from datetime import datetime

d = Dragon()

import matplotlib.pyplot as plt


def plot_sub(ax):
    plt.xticks([])
    plt.yticks([])
    plt.gca().set_aspect("equal", adjustable="box")

    ax.spines["bottom"].set_color("white")
    ax.spines["top"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["right"].set_color("white")


fig = plt.figure(figsize=(10, 10))

print("figure 1")
ax = fig.add_subplot(220 + 1)
d.run(N=2)
plot_sub(ax)

print("figure 2")
ax = fig.add_subplot(220 + 2)
d.run(N=4)
plot_sub(ax)

print("figure 3")
ax = fig.add_subplot(220 + 3)
d.run(N=5)
plot_sub(ax)

print("figure 4")
ax = fig.add_subplot(220 + 4)
d.run(N=6)
plot_sub(ax)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

plt.tight_layout(pad=5, w_pad=5, h_pad=5)
plt.savefig("Images/paper_4_" + now + ".png", dpi=250)
