# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:54:34 2020

@author: andre
"""

import json 
import geopy.distance

f=open("NHL_Arena_List.txt","r")
content=f.read()
f.close()

data=json.loads(content)

NHL_Teams=data.keys()
NHL_Arenas=data.values()
n_Teams=len(NHL_Teams)

#print(NHL_Arenas)

location=[]
NHL_Arena=[]

for i,key in enumerate(NHL_Teams):
    NHL_Arena=data[key]
    coords=[[NHL_Arena["lat"],NHL_Arena["long"]]]
    location=location+coords

#print(location)

Arena_Distance=[]
City_distances=[]

for i in range(n_Teams):
    coords_1=location[i]
    for j in range(n_Teams):
        coords_2=location[j]
        City_distances=City_distances+[int(geopy.distance.distance(coords_1, coords_2).km)]
    Arena_Distance=Arena_Distance+[City_distances]
    City_distances=[]
    
#print(Arena_Distance[0])
average_city_distance=[]

for i,key in enumerate(NHL_Teams):
    average_city_distance=average_city_distance+[int(sum(Arena_Distance[i])/n_Teams)]
    print("Avg. d. of ",key,"\n\t\t from other cities is\t",average_city_distance[i])
print("Most isolated city is",max(average_city_distance))
print("Least isolated city is",min(average_city_distance))


