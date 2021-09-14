# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:52:20 2017

@author: peter
"""

import csv
import numpy as np
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
from mpmath import mp
import geocoder

# load spreadsdata
data = []
with open("datauk.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter="\t", quotechar="|")
    for row in spamreader:
        data.append(row)


city = []
population = []
for row in data:
    city.append(row[0])
    pop = row[1].replace(",", "")
    if len(pop) > 0:
        population.append(float(pop))
    else:
        population.append(float(0))

# get countries latitude
# geolocator = Nominatim()
location = []
for c in city:
    print(c)
    try:
        g = geocoder.google(c + ", UK")
        location.append([float(g.lat), float(g.lng)])
    except:
        try:
            g = geocoder.google(c + ", UK")
            location.append([float(g.lat), float(g.lng)])
        except:
            print("Could not get")
            location.append([np.NaN, np.NaN])


# pop_sorted = [x for x in reversed(sorted(population))]
# city_sorted = [x for _,x in reversed(sorted(zip(population,city)))]
# location_sorted = [x for _,x in reversed(sorted(zip(population,location)))]

# make pie digits
# pi=[]
# mp.dps = 1000
# for i in range(1000):
#    d = mp.floor(mp.pi(1000)*10**(i)) - 10*mp.floor(mp.pi(1000)*10**(i-1))
#    pi.append(float(d))


fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111)

plt.xlim([-10, 5])
plt.ylim([48, 63])
# plot;
y = 1
for i in range(len(city)):
    print(i, y, ": ", city[i], location[i])
    if location[i][0] != "NoneType" and location[i][0] > -180:
        ax.text(
            np.round(location[i][1], 3),
            np.round(location[i][0], 3),
            str(y),  # +','+str(pi[i-7]),
            fontsize=np.max([2 * population[i] ** 0.5 / 10 ** 2, 6]),
        )
        y = y + 1

for i in range(10):
    ax.text(5, 60 - i * 0.2, str(i + 1) + ". " + city[i])

# plt.xticks([])
# plt.yticks([])
ax.set_axis_off()

ax.spines["bottom"].set_color("white")
ax.spines["top"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines["right"].set_color("white")

plt.savefig("Images/uk.png")
