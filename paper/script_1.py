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


fig = plt.figure(figsize=(20, 20))

print("figure 4")
ax = fig.add_subplot(110 + 1)
d.run(N=11)
plot_sub(ax)

now = datetime.now().strftime("%Y-%m-%d %H_%M_%S")

plt.tight_layout(pad=5, w_pad=5, h_pad=5)
plt.savefig("Images/paper_" + now + ".png", dpi=250)
