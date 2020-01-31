# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:54:34 2020

@author: andre
"""
#The purpose of this code is to study the distance between NHL arenas

import json 
import geopy.distance

#All required data is stored in the corresponding text file
f=open("NHL_Arena_List.txt","r") 
content=f.read()
f.close()

#We convert the string to a dictionary to improve processing speed
data=json.loads(content)

NHL_Teams=data.keys()
NHL_Arenas=data.values()
n_Teams=len(NHL_Teams)

#List designed to hold all the distances from 1 city to all the others
City_distances=[]
#List designed to hold all the lists of city distances (will serve for future reference)
Arena_Distance=[]

for i,key in enumerate(NHL_Teams):
    coords_1=(data[key]["lat"],data[key]["long"])
    for key1 in NHL_Teams:
        coords_2=(data[key1]["lat"],data[key1]["long"])
        City_distances=City_distances+[int(geopy.distance.distance(coords_1, coords_2).km)]
    Arena_Distance=Arena_Distance+[City_distances]
    #The average distance is added to the data of each arena
    data[key]["average_distance"]=int(sum(Arena_Distance[i])/n_Teams)
    #The City_distance is reset to an empty list for the next city
    City_distances=[]
    print("Avg. d. of ",key,"\n\t\t from other cities is\t",data[key]["average_distance"])



