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

City_distances=[]
Arena_Distance=[]

for i,key in enumerate(NHL_Teams):
    coords_1=(data[key]["lat"],data[key]["long"])
    for key1 in NHL_Teams:
        coords_2=(data[key1]["lat"],data[key1]["long"])
        City_distances=City_distances+[int(geopy.distance.distance(coords_1, coords_2).km)]
    Arena_Distance=Arena_Distance+[City_distances]
    data[key]["average_distance"]=int(sum(Arena_Distance[i])/n_Teams)
    City_distances=[]
    print("Avg. d. of ",key,"\n\t\t from other cities is\t",data[key]["average_distance"])



