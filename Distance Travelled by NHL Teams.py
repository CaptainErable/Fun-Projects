# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:59:19 2020

@author: andre
"""
#The purpose of this code is to study the distance between NHL arenas

import json 
import geopy.distance
import csv

""" 
Recovering Arena List
"""
f=open("NHL_Arena_List.txt","r") 
content=f.read()
f.close()

#String converted to dictionary to improve processing speed
data=json.loads(content)

NHL_Teams=data.keys()
n_Teams=len(NHL_Teams)

""" 
Recover NHL 19-20 Schedule
"""
Schedule_List=[]
    
with open('NHL_Schedule_19_20.csv', 'r') as file:
        my_reader = csv.reader(file, delimiter=',')
        for row in my_reader:
            Schedule_List=Schedule_List+[row]
            
Schedule_Length=len(Schedule_List)

""" 
Reciver each Team Calendar
"""
Team_Schedules={}

for key in NHL_Teams:
    Team_Schedules[key]=[]
    for i in range(Schedule_Length):
        if Schedule_List[i][2]==key or Schedule_List[i][3]==key:
            Team_Schedules[key]=Team_Schedules[key]+[Schedule_List[i]]

""" 
Calculate covered distance by one team throughout their calendar
"""
#Team_Schedules[key][0][2] is an away team
#Team_Schedules[key][0][3] is a home team

for key in NHL_Teams:
    distance=0
    #Initialization if Team is Away
    if Team_Schedules[key][0][2]==key:
            coords_1=(data[key]["lat"],data[key]["long"])
            key2=Team_Schedules[key][0][3]
            coords_2=(data[key2]["lat"],data[key2]["long"])
            distance=distance+int(geopy.distance.distance(coords_1, coords_2).km)
    for i in range(1,len(Team_Schedules[key])):
        #If Team is Away - return distance between arenas they were at (includes leaving Home)
        if Team_Schedules[key][i][2]==key:
            key2=Team_Schedules[key][i-1][3]
            coords_1=(data[key2]["lat"],data[key2]["long"])
            key2=Team_Schedules[key][i][3]
            coords_2=(data[key2]["lat"],data[key2]["long"])
            distance=distance+int(geopy.distance.distance(coords_1, coords_2).km)
        #If Team is Home, but previous game was Away - return distance between cities
        elif Team_Schedules[key][i][2]!=key and Team_Schedules[key][i-1][2]==key:
            key2=Team_Schedules[key][i-1][3]
            coords_1=(data[key2]["lat"],data[key2]["long"])
            coords_2=(data[key]["lat"],data[key]["long"])
            distance=distance+int(geopy.distance.distance(coords_1, coords_2).km)
    data[key]["total_distance"]=distance
    print(key,distance)