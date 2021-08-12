import googlemaps
from datetime import datetime
import numpy as np
from PIL import Image, ImageFilter

#Scirpt to make contour map of distance from london

#TODO save times in a json file so it can be loaded

GOOGLE_MAPS_API = 'XXXX'
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API)

# # Request directions via public transit
now = datetime.now()

# tl_cords = (60,-12)
# br_cords = (50,2)
tl_cords = (61,-12)
br_cords = (49,2)
dx = 0.5

N_x = int((tl_cords[0] - br_cords[0])/dx)
N_y = int((br_cords[1] - tl_cords[1])/dx)

Cords_x = np.random.uniform(tl_cords[0], br_cords[0], N_x)
Cords_y = np.random.uniform(tl_cords[1], br_cords[1], N_y)

coords = []
for i in range(N_x):
    for j in range(N_y):
        # coords.append((br_cords[0] + i*dx,tl_cords[1] + j*dx)
        coords.append([Cords_x[i], Cords_y[j]])

results = []
print('Started getting google resutls')
for i in range(0,int(N_x*N_y/100)):
    directions_result_matrix = gmaps.distance_matrix("London", #TODO add time of depart
                                     coords[i*100:(i+1)*100],
                                     mode="driving", #transit, driving, walking, bicycling
                                     departure_time=now)
    for j in range(0,len(directions_result_matrix['rows'][0]['elements'])):
        results.append([directions_result_matrix['rows'][0]['elements'][j],coords[i*100:(i+1)*100][j]])
    print(str(i) + '/' + str(int(N_x*N_y/100)),end='\r')
print('Finished getting google resutls')

import csv
with open('london.csv','a') as file:
    writer = csv.writer(file)
    for block in results:
        print(block)
        # for i in range(0,len(block[0])):
        if 'duration' in block[0].keys():
            print(block[0]['duration']['value'])
            print(block[1])
            row_save = [block[0]['duration']['value'] , block[1][0] , block[1][1]]
        else:
            row_save = [-1, block[1][0], block[1][1]]
        print(row_save)
        writer.writerow(row_save)



# print(directions_result_matrix['rows'][0]['elements'])
# directions_result_matrix['rows'][0]['elements'][1]['duration']['text']
