# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:50:55 2017

script to make picture fom digitis of pi

@author: DUDFI00P
"""

# import matplotlib as mpl
# mpl.rc('text', usetex=True)
# mpl.rcParams['text.latex.preamble']=[r"\usepackage{amssymb}",
#                                    r"\usepackage{amsmath}"]

# from mpmath import mp
# import pidigits
import numpy as np
import os
import matplotlib.pyplot as plt

# from PIL import Image
from mnist import MNIST
from datetime import datetime

# from matplotlib import rc
import csv
import json


m = 200
mm = 20
# N=200
# rows=10
# cols=10
# N = rows*cols
now = datetime.now().strftime("%Y-%m-%d")

colors = {}
colors["0"] = (255, mm, mm)
colors["1"] = (255, m, mm)
colors["2"] = (m, 255, mm)
colors["3"] = (mm, 255, mm)
colors["4"] = (mm, 255, m)
colors["5"] = (mm, m, 255)
colors["6"] = (mm, mm, 255)
colors["7"] = (m, mm, 255)
colors["8"] = (255, mm, m)
colors["9"] = (m, m, m)

#
local_folder = f"{os.path.dirname(os.path.realpath(__file__))}/../MNIST"
mndata = MNIST(local_folder)
mndata.gz = True
images, labels = mndata.load_testing()
# mndata.load_testing()
class Digits:
    def __init__(self, letters, rows=10, cols=10):

        self.letters = letters
        self.rows = rows
        self.cols = cols
        self.N = rows * cols

        self.fullname = ""
        for l in letters:
            self.fullname = self.fullname + l

    def make_letter(self, letter):

        self.letter = letter

        results = "{"
        with open("data/" + letter + ".txt", newline="") as inputfile:
            for row in csv.reader(inputfile):
                results = results + row[0] + ","
        # results = results[0:31] +' \'}'
        results = results[0:-1] + "}"
        results = results.replace("'", '"').replace("\\", "\\\\")

        data = json.loads(results)

        self.letter_list = str(data["digits"])
        self.name = data["name"]
        self.description = data["description"]

        if "equation" in data.keys():
            self.equation = data["equation"]
        else:
            self.equation = ""

        # make image
        self.make_image()

    def make_image(self):

        N = self.N
        rows = self.rows
        cols = self.cols

        letter_array = np.zeros((rows, cols))
        letter_array_color = np.zeros((rows, cols))
        image_array = np.zeros((28 * rows, 28 * cols, 3))

        j = 0
        # make image array
        for i in range(self.N):

            x = int(i % cols)
            y = int((i - x) / cols)

            letter_array[y, x] = int(self.letter_list[i])

            j = j + 1
            while letter_array[y, x] != labels[j]:
                j = j + 1

            image_one = images[j]
            image_one = 255 - np.resize(image_one, (28, 28))

            image_array[28 * y : 28 + 28 * y, 28 * x : 28 + 28 * x, 0] = image_one
            image_array[28 * y : 28 + 28 * y, 28 * x : 28 + 28 * x, 1] = image_one
            image_array[28 * y : 28 + 28 * y, 28 * x : 28 + 28 * x, 2] = image_one

            if i == 1:
                image_array[23:25, 26:28, :] = 0

        # make letter color array
        for i in range(N):

            x = int(i % cols)
            y = int((i - x) / cols)

            if x < cols - 1:
                if letter_array[y, x] == letter_array[y, x + 1]:
                    letter_array_color[y, x] = 1
                    letter_array_color[y, x + 1] = 1

            if y < rows - 1:
                if letter_array[y, x] == letter_array[y + 1, x]:
                    letter_array_color[y, x] = 1
                    letter_array_color[y + 1, x] = 1

            if x < cols - 1 and y < rows - 1:
                if letter_array[y, x] == letter_array[y + 1, x + 1]:
                    letter_array_color[y, x] = 1
                    letter_array_color[y + 1, x + 1] = 1
                if letter_array[y, x + 1] == letter_array[y + 1, x]:
                    letter_array_color[y, x + 1] = 1
                    letter_array_color[y + 1, x] = 1

        for i in range(N):

            x = int(i % cols)
            y = int((i - x) / cols)

            # background_color='black'
            if letter_array_color[y, x] == 1:
                # background_color='red'

                temp_array = image_array[28 * y : 28 + 28 * y, 28 * x : 28 + 28 * x]
                idx = image_array[28 * y : 28 + 28 * y, 28 * x : 28 + 28 * x, 0] < 255

                temp_array[idx, 0] = (
                    temp_array[idx, 0]
                    + (1 - temp_array[idx, 0] / 255) * colors[str(int(letter_array[y, x]))][0]
                )
                temp_array[idx, 1] = (
                    temp_array[idx, 1]
                    + (1 - temp_array[idx, 1] / 255) * colors[str(int(letter_array[y, x]))][1]
                )
                temp_array[idx, 2] = (
                    temp_array[idx, 2]
                    + (1 - temp_array[idx, 2] / 255) * colors[str(int(letter_array[y, x]))][2]
                )

                image_array[28 * y : 28 + 28 * y, 28 * x : 28 + 28 * x] = temp_array

        self.image_array = image_array

    def plot_digits(
        self,
        fig=None,
        N_letters=1,
        current_letter=0,
        add_text=False,
        add_description=False,
        add_equation=False,
        add_mart=False,
        save_fig=False,
        name=None,
    ):

        self.make_letter(self.letters[current_letter])

        # if fig==None:
        #    fig = plt.figure(figsize=(7,10))

        ax0 = plt.subplot2grid((5, N_letters), (0, current_letter), rowspan=4, colspan=1)
        ax0.imshow(self.image_array / 255, "gray")

        # if self.letter in ['e','a','c','f','l','i']:

        letter_latex = "$" + self.name + "$"

        # else:
        #    letter_latex = '$\\'+self.letter+'$'
        if name == None:
            if self.letter != self.name:
                plt.title(self.letter + " (" + letter_latex + ")", fontsize=80)
            else:
                plt.title(self.letter, fontsize=80)
        else:
            # plt.title(r"$\bf{" + letter_latex.replace('$','') + '}$' + name[1:] , fontsize=80)
            plt.title(
                r"$" + letter_latex.replace("$", "") + "$" + " " * len(name),
                fontsize=80,
                color="black",
            )
            if "H" in letter_latex:
                drift = 80
            else:
                drift = 30

            print(letter_latex)
            plt.text(
                self.cols / 2 * 28 - len(name) * 20 / 2 + drift,
                -5,
                name[1:],
                fontsize=60,
                color="grey",
            )

            print(self.cols)
            print(self.image_array.shape)

        plt.xticks([], [])
        plt.yticks([], [])
        ax0.spines["bottom"].set_color("white")
        ax0.spines["top"].set_color("white")
        ax0.spines["right"].set_color("white")
        ax0.spines["left"].set_color("white")

        ax1 = plt.subplot2grid((5, N_letters), (4, current_letter))
        if add_text:
            # ax1.text(0.1,-0.1,'The digits of '+letter_latex+' displayed with the MNIST database of handwritten \n '
            #                                                 'numbers. Similar adjacent digits in the grid are highlighted.')
            ax1.text(
                0.1,
                -0.1,
                "The digits are displayed with the MNIST database of handwritten numbers. \n"
                "Similar adjacent digits in the grid are highlighted.",
            )
        if add_description:
            ax1.text(0.1, 0.6, self.description.replace("\\n", "\n"))
        if add_equation:
            if self.equation != "":
                ax1.text(0.1, 0.4, "$" + self.equation + "$")
        if add_mart:
            ax1.text(0.1, -0.3, now + " $M\\alpha r \\tau$")

        plt.xticks([], [])
        plt.yticks([], [])
        ax1.spines["bottom"].set_color("white")
        ax1.spines["top"].set_color("white")
        ax1.spines["right"].set_color("white")
        ax1.spines["left"].set_color("white")

        # if filename==None:
        if add_text:
            filename = "images/" + now + "-" + self.fullname + "_notext.png"
        else:
            filename = "images/" + now + "-" + self.fullname + ".png"

        if save_fig == 1:
            print(filename)
            plt.savefig(filename, dpi=300)

        self.plt = plt
