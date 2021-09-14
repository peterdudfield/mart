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
with open("countrydata2.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for row in spamreader:
        data.append(row)

# load spreadsdata
data2 = []
Capitals = {}
with open("datacaptials.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for row in spamreader:
        data2.append(row)
        if row[1].replace('"', "") == "Washington":
            Capitals[row[0].replace('"', "")] = "Washington, DC"
        if row[1].replace('"', "") == "United Kingdom; England":
            Capitals[row[0].replace('"', "")] = "United Kingdom"
        else:
            Capitals[row[0].replace('"', "")] = row[1].replace('"', "")

country = []
population = []
for row in data[5:]:
    if row[0][1:-1] == "Russian Federation":
        country.append("Russia")
    else:
        country.append(row[0].replace('"', ""))
    pop = row[-2][1:-1]
    if len(pop) > 0:
        population.append(float(pop))
    else:
        population.append(float(0))

# get countries latitude
# geolocator = Nominatim()
location = []
for c in country:
    print(c)
    try:
        # geolocator.country_bias = c
        # location_one = geolocator.geocode(Capitals[c])
        # location.append([location_one.latitude,location_one.longitude])

        g = geocoder.google(Capitals[c])
        location.append([float(g.lat), float(g.lng)])
    except:
        print("Could not get")
        location.append([np.NaN, np.NaN])


pop_sorted = [x for x in reversed(sorted(population))]
country_sorted = [x for _, x in reversed(sorted(zip(population, country)))]
location_sorted = [x for _, x in reversed(sorted(zip(population, location)))]

# make pie digits
# pi=[]
# mp.dps = 1000
# for i in range(1000):
#    d = mp.floor(mp.pi(1000)*10**(i)) - 10*mp.floor(mp.pi(1000)*10**(i-1))
#    pi.append(float(d))


fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111)

plt.xlim([-180, 200])
plt.ylim([-90, 90])
# plot;
y = 1
for i in range(7, len(country_sorted)):
    print(i, y, ": ", country_sorted[i], location_sorted[i])
    if location_sorted[i][0] != "NoneType" and location_sorted[i][0] > -180:
        ax.text(
            np.round(location_sorted[i][1], 3),
            np.round(location_sorted[i][0], 3),
            str(y),  # +','+str(pi[i-7]),
            fontsize=np.max([pop_sorted[i - 7] ** 0.5 / 10 ** 3, 6]),
        )
        y = y + 1


# plt.xticks([])
# plt.yticks([])
ax.set_axis_off()

ax.spines["bottom"].set_color("white")
ax.spines["top"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines["right"].set_color("white")

plt.savefig("Images/world.png")
