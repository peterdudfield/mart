from apollon import ApollonianGasket, Circle
from plotting import plot_circle
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

a = ApollonianGasket(1,2,3)
a.generate(5)


fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

colours = ['#ff4e50','#fc913a','#f9d62e','#8bc34a','#e2f4c7','#fd5a40']
colours = ['#83DDD6','#8BEAAF','#F7F396','#F2C9C9','#ACA7C4','#83DDD6','#8BEAAF','#F7F396']

c_idx = 0
max_x = 0
max_y = 0
min_x = 0
min_y = 0
for circle in a.genCircles:

    print(circle)

    mx = circle.m.real
    my = circle.m.imag
    r = np.abs(circle.r.real)

    if mx + r >max_x:
        max_x = mx+r
    if my + r > max_y:
        max_y = my+r
    if mx-r < -min_x:
        min_x = r-mx
    if np.abs(my-r) > min_y:
        min_y = np.abs(my-r)

    print(my)
    print(mx)
    print(r)
    print(max_x, max_y)
    print(min_x, min_y)

    c = plot_circle(mx, my, r, colours[c_idx])
    c_idx += 1
    if c_idx == len(colours):
        c_idx = 0

    ax.add_artist(c)

print(max_x, max_y)
print(min_x, min_y)
extra = 1.2
ax.set_xlim((-min_x-0.1 - extra, max_x+0.1 + extra))
ax.set_ylim((-min_y-0.1, max_y+0.1))
plt.axis('off')

plt.text(max_x-0.5, -min_y, r'$\mathcal{M} \alpha r \tau$ ' + datetime.now().strftime("%Y-%m-%d"))

fig.savefig('Images/plotcircles_'+str(datetime.now())+'.png')