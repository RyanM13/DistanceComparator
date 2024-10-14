import math
import numpy as np

def Manhattan(x1,y1,x2,y2):

    return abs(x1-x2) + abs(y1-y2)

def Euclidian(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

Data = np.loadtxt("distances.txt",delimiter=',')

x = Data[:, 0]
y = Data[:, 1]

TotalManhattanDist = 0
TotalEucldianDist = 0
avg = 0

differences = []
difference = 0

for i in range(len(x) - 1):  
    TotalManhattanDist = Manhattan(x[i], y[i], x[i+1], y[i+1])
    TotalEucldianDist = Euclidian(x[i], y[i], x[i+1], y[i+1])

    difference = abs(TotalManhattanDist - TotalEucldianDist)
    differences.append(difference)

avg = sum(differences) / len(differences)
print("The average distance difference is about: ", avg, '\n')

for i in range(len(x) - 1):  
    print("Manhattan: ",Manhattan(x[i], y[i], x[i+1], y[i+1]))
    print("Euclidian: ", Euclidian(x[i], y[i], x[i+1], y[i+1]))
    difference = Manhattan(x[i], y[i], x[i+1], y[i+1]) - Euclidian(x[i], y[i], x[i+1], y[i+1]) 
    print("Difference: ", difference)
    print(" ")


avg = sum(differences) / len(differences)







    