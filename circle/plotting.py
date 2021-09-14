import matplotlib.pyplot as plt


def plot_circle(mx, my, r, colour="r"):

    circle = plt.Circle((mx, my), r, color=colour, fill=False)

    return circle
