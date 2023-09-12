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

def comparator(testpoints,pichu,pikachu):
  for i in testpoints:
    print(i)
    x1 = i[0]
    y1 = i[1]
    for index in pichu:
      x2 = index[0]
      y2 = index[1]


# d=√((x2 – x1)² + (y2 – y1)²) 
# Vad jag vill göra är att kolla avståndet ifrån testpunkt till alla punkter i pichu och pikachu.
# Sen tar jag medianen av avståndet emellan pichu och pikachu till testpunkt och assignar label till den medianen som var närmast testpunkten
x1 = 1
x2 = 2

y1 = 1
y2 = 2

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(distance)

comparator(testpoints, pichu, pikachu)