import googlemaps
from datetime import datetime
import numpy as np
from PIL import Image, ImageFilter

#
# #Scirpt to make contour map of distance from london
#
# #TODO save times in a json file so it can be loaded
#
# GOOGLE_MAPS_API = 'XXXX'
# gmaps = googlemaps.Client(key=GOOGLE_MAPS_API)
#
# # # Request directions via public transit
# now = datetime.now()
#
# tl_cords = (60,-12)
# br_cords = (50,2)
tl_cords = (61, -12)
br_cords = (49, 2)
dx = 0.1

N_x = int((tl_cords[0] - br_cords[0]) / dx)
N_y = int((br_cords[1] - tl_cords[1]) / dx)
#
# N_x = np.random.uniform(tl_cords[0], br_cords[0],10)
# N_y = np.random.uniform(tl_cords[1], br_cords[1],10)
#
# coords = []
# for i in range(N_x):
#     for j in range(N_y):
#         coords.append((br_cords[0] + i*dx,tl_cords[1] + j*dx))
#
# results = []
# for i in range(0,int(N_x*N_y/100)):
#     directions_result_matrix = gmaps.distance_matrix("London",
#                                      coords[i*100:(i+1)*100],
#                                      mode="driving", #transit, driving, walking, bicycling
#                                      departure_time=now)
#     for item in directions_result_matrix['rows'][0]['elements']:
#         results.append(item)
#     print(str(i) + '/' + str(int(N_x*N_y/100)),end='\r')

import pandas as pd

df = pd.read_csv("london.csv", names=["distance", "x", "y"])


def find_distance(x, y, df, n=1):

    df["r"] = ((df["x"] - x) ** 2 + (df["y"] - y) ** 2) ** 0.5
    df.index = df["r"]
    df_sort = df.sort_index(by="r")
    # print(df_sort.head())
    # print(df_sort['distance'].values[0])
    # df_sort = df.sort_values(by='r')
    # print(df_sort['distance'][0:5], np.sum(df_sort['distance'][0:5])/n)
    distance = np.sum(df_sort["distance"].values[0:n]) / n

    if (df_sort["distance"].values[0:n] == -1).sum() > 0:
        distance = -1

    print(x, y, distance, df_sort["x"].values[0], df_sort["y"].values[0])

    return distance


# print(directions_result_matrix['rows'][0]['elements'])
# directions_result_matrix['rows'][0]['elements'][1]['duration']['text']


distance_matrix = np.zeros((N_x, N_y))
n = 0
for i in range(0, N_x):
    for j in range(0, N_y):

        x, y = br_cords[0] + i * dx, tl_cords[1] + j * dx

        d = find_distance(x, y, df)

        distance_matrix[i][j] = d

        n = n + 1

limit_hours = 14

distance_matrix[distance_matrix > 3600 * limit_hours] = 3600 * limit_hours
distance_matrix /= 3600

# image = Image.fromarray(distance_matrix/np.max(np.max(distance_matrix))*256)
# image = image.resize((N_x*2,N_y*2))
#
# distance_matrix = np.array(image)
#
# import scipy.signal
#
# im = distance_matrix/np.max(np.max(distance_matrix))   # normalise to 0-1, it's easier to work in float space
#
# # make some kind of kernel, there are many ways to do this...
# t = 1 - np.abs(np.linspace(-1, 1, 4))
# kernel = t.reshape(4, 1) * t.reshape(1, 4)
# kernel /= kernel.sum()   # kernel should sum to 1!  :)
#
# # convolve 2d the kernel with each channel
# im_out = scipy.signal.convolve2d(im[:,:], kernel, mode='same')
#
# # stack the channels back into a 8-bit colour depth image and plot it
# im_out = (im_out * 255).astype(np.uint8)
#
# # image = Image.fromarray(distance_matrix/np.max(np.max(distance_matrix))*256)
# # image = image.resize((N_x*2,N_y*2))
# # image = image.filter(ImageFilter.BLUR)
#
# # distance_matrix = np.array(image)

import matplotlib.pyplot as plt

plt.imshow(distance_matrix)
plt.gca().invert_yaxis()
# plt.gca().invert_xaxis()
plt.colorbar()
# plt.show()
plt.savefig("london.png")
#
