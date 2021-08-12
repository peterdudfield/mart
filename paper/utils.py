N_folders = 1
import matplotlib.pyplot as plt
import numpy as np


class Dragon():

    def run(self, L=0.9, N=7):

        lines = []
        lines.append([1, -1, 1, 0, 0])
        lines.append([1, 0, 0, 0, 1])

        self.lines = lines

        self.L = L
        self.N = N

        for i in range(0, self.N):

            print('Making new lines ' + str(i))
            new_lines = self.lines.copy()
            n = len(self.lines)
            for i in range(0, len(self.lines)):
                # new_lines.append(line)
                new_line = self.r90(self.lines[::-1][i], n + i)
                new_lines.append(new_line)

            lines = new_lines.copy()
            self.lines = self.move_lines(lines)

        print('Plotting lines')
        self.plot_lines(lines)

    def r90(self, line, m):
        x1, y1, x2, y2, n = line

        new_line = [y1, -x1, y2, -x2, m]
        return new_line

    def smooth_lines(self, line1, line2):
        x1_1, y1_1, x2_1, y2_1, n_1 = line1
        x1_2, y1_2, x2_2, y2_2, n_2 = line2
        L = self.L


        # end of first line eqauls start of second line
        if x2_1 == x1_2 and y2_1 == y1_2:
            line1 = line1
            line2 = line2

        # start of first line equals start of second line
        if x1_1 == x1_2 and y1_1 == y1_2:
            line1 = [x2_1, y2_1, x1_1, y1_1, n_1]
            line2 = line2

        # end of first line equals end of second line
        if x2_1 == x2_2 and y2_1 == y2_2:
            line1 = line1
            line2 = [x2_2, y2_2, x1_2, y1_2, n_2]

        # start of first line equals end of second line
        if x1_1 == x2_2 and y1_1 == y2_2:
            line1 = [x2_1, y2_1, x1_1, y1_1, n_1]
            line2 = [x2_2, y2_2, x1_2, y1_2, n_2]

        x1_1, y1_1, x2_1, y2_1, n_1 = line1
        x1_2, y1_2, x2_2, y2_2, n_2 = line2

        x1 = x1_1 * (1 - L) + x2_1 * L
        x2 = x2_2 * (1 - L) + x1_2 * L
        y1 = y1_1 * (1 - L) + y2_1 * L
        y2 = y2_2 * (1 - L) + y1_2 * L

        x1_1 = x2_1 * (1 - L) + x1_1 * L
        y1_1 = y2_1 * (1 - L) + y1_1 * L

        x2_1 = x1
        y2_1 = y1

        line_new = [x1, y1, x2, y2, (n_1 + n_2) / 2]
        line1 = [x1_1, y1_1, x2_1, y2_1, n_1]

        return line1, line_new

    def plot_lines(self, lines):
        # fig = plt.figure()
        # ax = plt.axes()

        for i in range(0, int(len(lines))):
            x1_1, y1_1, x2_1, y2_1, n = lines[i]
            # x1_2, y1_2, x2_2, y2_2, n = lines[i+1]

            if i < len(lines) - 1:
                line1, line_new = self.smooth_lines(lines[i], lines[i + 1])
            else:
                proxy_line = [x2_1, y2_1, x2_1, y2_1, n]
                line1, line_new = self.smooth_lines(lines[i], proxy_line)

            x1_1, y1_1, x2_1, y2_1, n = line1
            x1, y1, x2, y2, n = line_new


            c = [i / len(lines), 0, 0]

            if i < len(lines) - 1:
                plt.plot([x1, x2], [y1, y2], color=c,solid_capstyle='round',lw=2)
            plt.plot([x1_1, x2_1], [y1_1, y2_1], color=c,solid_capstyle='round',lw=2)

    def move_lines(self, lines):
        min_x = 1
        min_y = 1

        for line in lines:
            x1, y1, x2, y2, n = line

            if x1 < min_x:
                min_x = x1
            if x2 < min_x:
                min_x = x2
            if y1 < min_y:
                min_y = y1
            if y2 < min_x:
                min_y = y2

        x0 = min_x
        y0 = min_y

        x0 = np.min([lines[-1][0], lines[-1][2]])
        y0 = np.min([lines[-1][1], lines[-1][3]])

        new_lines = []

        for line in lines:
            x1, y1, x2, y2, n = line
            new_line = [x1 - x0, y1 - y0, x2 - x0, y2 - y0, n]
            new_lines.append(new_line)

        return new_lines


def __main__():
    d = Dragon()
    d.run()
