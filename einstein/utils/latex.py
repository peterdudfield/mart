# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:06:33 2018

@author: DUDFI00P
"""

import csv
from datetime import datetime


def read_tex(tex_file, rm_first_rows=22, rm_last_rows=6):

    results = []
    with open("data/" + tex_file, newline="") as inputfile:
        for row in csv.reader(inputfile, delimiter="\t"):
            results.append(row)

    # remove first 19 rows and last 5
    results = results[rm_first_rows:-rm_last_rows]

    # change new line to \n
    text_str = ""
    for para in results:
        for line in para:
            if len(line) > 1:
                text_str = text_str + line[0].lower() + line[1:]
        text_str = text_str + " \n "

    # format
    text_str = text_str.replace(". ", " . ")
    text_str = text_str.replace(", ", " , ")
    text_str = text_str.replace(".,", ". ,")
    text_str = text_str.replace("\r\n", " \n ")
    text_str = text_str.replace("\\subsection", " \\subsection")
    text_str = text_str.replace("\\section", " \\section")
    text_str = text_str.replace('"', "")
    # text_str = text_str.replace('(',', ')
    # text_str = text_str.replace(')',', ')

    text_str = text_str.replace("  ", " ")
    text_str = text_str.replace("  ", " ")
    text_str = text_str.replace("  ", " ")

    return text_str


def make_tex(main_str, model_str):

    latex_str = [
        "\\documentclass{article} % Use the custom resume.cls style",
        "\\usepackage{geometry} % Document margins",
        "\\usepackage{multicol}",
        "\\usepackage{color}",
        "\\usepackage{float}",
        "%\\usepackage{psfrag}",
        "\\usepackage{graphicx}",
        "",
        "",
        "\\begin{document}",
        "",
        "\\begin{center}",
        "\\Huge",
        "\\textbf{On the electrodynamics of moving bodies - " + model_str + "}",
        "\\end{center}",
        "\\begin{center}",
        "\\textbf{Mart}",
        "\\end{center}",
        "",
    ]

    for para in list(main_str.split("\n")):
        latex_str.append(para)

    latex_str = latex_str + ["", "\t", "\\end{document}"]

    now = datetime.now().strftime("_%Y-%m-%d_%H_%M_%S")
    filename = "results/" + model_str + now + ".tex"

    with open(filename, "w") as text_file:
        for para in latex_str:
            text_file.write(para + " \n ")
