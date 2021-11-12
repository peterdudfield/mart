import numpy as np
from matplotlib import pyplot as plt


def make_tree(Theta1, Theta2, L_d, R_d, size, ax, scalefactor=2, N_layers=6):
    # first tree
    # print('Making first points')
    first_points = [[0, 0], [0, 1]]
    lines = [first_points]

    lines_layer = []
    lines_layer.append(lines)
    for i in range(N_layers):
        lines = make_lines(str(i + 2), lines, i, L_d, R_d, Theta1, Theta2, scalefactor)
        lines_layer.append(lines)

    # add lines to plot
    for i in range(N_layers + 1):
        print("Adding lines to plot:" + str(i))
        j = 1
        for line in lines_layer[i]:
            print(str(j) + "/" + str(len(lines_layer[i])), end="\r")
            j = j + 1
            if i > 4:
                linewidth = 1.7 / ((i - 4) ** 0.4)
            else:
                linewidth = 2
            plt.plot(
                [line[0][0], line[1][0]],
                [line[0][1], line[1][1]],
                make_color(i),
                solid_capstyle="round",
                linewidth=linewidth,
            )

    ax.spines["bottom"].set_color("white")
    ax.spines["top"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["right"].set_color("white")

    plt.xlim([-size / 2, size / 2])
    plt.ylim([-0.2, size - 0.2])
    plt.xticks([])
    plt.yticks([])
    # ax.spines['bottom'].set_color('white')
    # ax.spines['top'].set_color('white')
    # ax.spines['left'].set_color('white')
    # ax.spines['right'].set_color('white')


def make_color(layer):

    h = 1 / (1.2 ** (layer))

    # green = (0,255,0)
    # brown = (51,0,0)

    color = (int(51 * h), int(255 * (1 - h)), 50)
    hex_color = "#%02x%02x%02x" % color

    return hex_color


def make_lines(layer_str, lines, layer, L_d, R_d, Theta1, Theta2, scalefactor):
    # print('Making ' + layer_str +' lines')

    lines_new = []
    for i in range(0, len(lines)):

        line = lines[i]

        new_points = make_points_from_line(
            line[0], line[1], layer, L_d, R_d, Theta1, Theta2, scalefactor
        )

        # lines_new.append([line[0],new_points[1]])
        lines_new.append([new_points[1], new_points[3]])
        lines_new.append([new_points[0], new_points[2]])
        if line_length(new_points[0], line[1]) > 0.001:
            lines_new.append([new_points[0], line[1]])

    return lines_new


def line_length(p1, p2):

    s = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    return s


def make_points_from_line(p1, p2, level, L_d, R_d, Theta1, Theta2, scalefactor):
    x1 = p1[0] * (1 - L_d) + p2[0] * L_d
    y1 = p1[1] * (1 - L_d) + p2[1] * L_d

    x2 = p1[0] * (1 - R_d) + p2[0] * R_d
    y2 = p1[1] * (1 - R_d) + p2[1] * R_d

    rotation = np.angle(complex(p2[0] - p1[0], p2[1] - p1[1]))

    height = 1 / (scalefactor ** (level + 1))

    x3 = x1 + height * np.cos(rotation + Theta1)
    y3 = y1 + height * np.sin(rotation + Theta1)

    x4 = x2 + height * np.cos(rotation - Theta2)
    y4 = y2 + height * np.sin(rotation - Theta2)

    t = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

    return t