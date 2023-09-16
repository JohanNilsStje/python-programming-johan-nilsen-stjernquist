import csv
import matplotlib.pyplot as plt
import numpy as np
import math
#Reads in the datapoints
file = open("Labb2\datapoints.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

### Variables ###
#Two lists that will contain pikachus and pichus
pikachu = []
pichu = []
#Testpoints
testpoints = [[25,32],[24.2,31.5],[22,34],[20.5,34]]
datastorage = []

#Data sorter/separator fixes the " 0" and " 1" from import of csv file
for i in data:
  if i[2] in " 0":
    i[2] = 0
    pichu.append(i)
  elif i[2] in " 1":
    i[2] = 1
    pikachu.append(i)

print(len(pikachu)) #75 pikachus
print(len(pichu)) #75 pichus


#Can turn this into 1 block of code instead of 2 by making 1 big dataset or making a function that can take pichu and pikachu and still plt.scatter it
#Puts all the pichu points on plot
for i in pichu:
  x = float(i[0])
  y = float(i[1])
  plt.scatter(x,y, color = 'blue')
#Puts all the pikachu points on plot
for i in pikachu:
  x = float(i[0])
  y = float(i[1])
  plt.scatter(x,y, color = 'orange')

#Draws the plot
plt.show()
#NEW TRY!!

for test in testpoints:
  print(f"{test} point")
  x1 = test[0]
  y1 = test[1]
  

#Old try
#def comparator(testpoints,db1,db2):
#  for i in testpoints:
#    print(i)
#    x1 = float(i[0])
#    y1 = float(i[1])
#    for index in db1:
#      x2 = float(index[0])
#      y2 = float(index[1])
#      compare(x1,x2,y1,y2)
#    for index in db2:
#      x2 = float(index[0])
#      y2 = float(index[1])
#      compare(x1,x2,y1,y2)

#def compare(x1,x2,y1,y2):
#  distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
#  datastorage.append(distance)


#comparator(testpoints[0],pichu,pikachu)
#print(pikachu[0])
# d=√((x2 – x1)² + (y2 – y1)²) 

# Vad jag vill göra är att kolla avståndet ifrån testpunkt till alla punkter i pichu och pikachu.
# Sen tar jag medianen av avståndet emellan pichu och pikachu till testpunkt och assignar label till den medianen som var närmast testpunkten


#comparator(testpoints, pikachu)
#print(len(datastorage))
#nam = 0
#for num in datastorage:
#  nam = num + nam

#print(nam / len(datastorage))*/