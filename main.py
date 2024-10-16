import math
import numpy as np
from Difference import Difference

def Manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def Euclidean(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def Slope(x1, y1, x2, y2):
    if x2 - x1 == 0:  # Avoid division by zero for vertical lines
        return float('inf')  # Representing an infinite slope
    return abs((y2 - y1) / (x2 - x1))

# Load data from distances.txt
Data = np.loadtxt("distances.txt", delimiter=',')
diff = Difference()

x = Data[:, 0]
y = Data[:, 1]

TotalManhattanDist = 0
TotalEuclideanDist = 0
overallAvg = 0
slopeAvg = 0

differences = []
HorizontalDiff = []
VerticalDiff = []
SteepDiff = []
ShallowDiff = []

diffMan = Difference()
diffEuc = Difference()
print("Large distance")
for i in range(len(x) - 1):
    manhattan_dist = Manhattan(x[i], y[i], x[i+1], y[i+1])
    euclidean_dist = Euclidean(x[i], y[i], x[i+1], y[i+1])
    slope = Slope(x[i], y[i], x[i+1], y[i+1])

    # Large distances
    if manhattan_dist > 500 and euclidean_dist > 500:
        
        if slope < 0.1:
            # Almost Horizontal
            difference = manhattan_dist - euclidean_dist
            HorizontalDiff.append(difference)
        elif 0.1 <= slope < 1:
            # Shallow Slope
            difference = manhattan_dist - euclidean_dist
            ShallowDiff.append(difference)
        elif 1 <= slope < 10:
            # Steep Slope
            difference = manhattan_dist - euclidean_dist
            SteepDiff.append(difference)
        else:
            # Almost Vertical
            difference = manhattan_dist - euclidean_dist
            VerticalDiff.append(difference)
if len(HorizontalDiff) > 0:
    slopeAvg = sum(HorizontalDiff) / len(HorizontalDiff)
    print("Horizontal slope avg: ", slopeAvg,'\n')
else:
    pass
if len(ShallowDiff) > 0:
    slopeAvg = sum(ShallowDiff)/ len(ShallowDiff)
    print("Shallow slope avg: " ,slopeAvg,'\n')
else:
    pass
if len(SteepDiff) > 0:
    slopeAvg = sum(SteepDiff) / len(SteepDiff)
    print("Steep slope avg: ", slopeAvg,'\n')
else: 
    pass
if len(VerticalDiff) > 0:
    slopeAvg = sum(VerticalDiff)/ len(VerticalDiff)
    print("Vertical slope avg: " ,slopeAvg,'\n')
else: 
    pass
    
print("Small Distance")
for i in range(len(x) - 1):
    manhattan_dist = Manhattan(x[i], y[i], x[i+1], y[i+1])
    euclidean_dist = Euclidean(x[i], y[i], x[i+1], y[i+1])
    slope = Slope(x[i], y[i], x[i+1], y[i+1])

    # Small distances
    if manhattan_dist <= 500 and euclidean_dist <= 500:
        
        if slope < 0.1:
            # Almost Horizontal
            difference = manhattan_dist - euclidean_dist
            HorizontalDiff.append(difference)
        elif 0.1 <= slope < 1:
            # Shallow Slope
            difference = manhattan_dist - euclidean_dist
            ShallowDiff.append(difference)
        elif 1 <= slope < 10:
            # Steep Slope
            difference = manhattan_dist - euclidean_dist
            SteepDiff.append(difference)
        else:
            # Almost Vertical
            difference = manhattan_dist - euclidean_dist
            VerticalDiff.append(difference)
        
        # Print averages for small distances
if len(HorizontalDiff) > 0:
    slopeAvg = sum(HorizontalDiff) / len(HorizontalDiff)
    print("Horizontal slope avg: ", slopeAvg, '\n')
else: 
    pass
if len(ShallowDiff) > 0:
    slopeAvg = sum(ShallowDiff) / len(ShallowDiff)
    print("Shallow slope avg: ", slopeAvg, '\n')
else: 
    pass
if len(SteepDiff) > 0:
    slopeAvg = sum(SteepDiff) / len(SteepDiff)
    print("Steep slope avg: ", slopeAvg, '\n')
else: 
    pass
if len(VerticalDiff) > 0:
    slopeAvg = sum(VerticalDiff) / len(VerticalDiff)
    print("Vertical slope avg: ", slopeAvg, '\n')


            

for i in range(len(x) - 1):
    manhattan_dist = Manhattan(x[i], y[i], x[i+1], y[i+1])
    euclidean_dist = Euclidean(x[i], y[i], x[i+1], y[i+1])
    difference = abs(manhattan_dist - euclidean_dist)
    differences.append(difference)

avg_difference = sum(differences) / len(differences)
print(" ")
print("Overall Difference")
print("The average overall distance difference is:", avg_difference, '\n')


print("Data")
for i in range(len(x) - 1):
    diffMan.setDistance(Manhattan(x[i], y[i], x[i+1], y[i+1]))
    diffEuc.setDistance(Euclidean(x[i], y[i], x[i+1], y[i+1]))
    
    print("Manhattan:", diffMan.getDistance())
    print("Euclidean:", diffEuc.getDistance())
    print("Difference:", diffMan.getDistance() - diffEuc.getDistance())
    print("Slope:", Slope(x[i], y[i], x[i+1], y[i+1]))
    print("Points: ",x[i], y[i], x[i+1], y[i+1])
    print(" ")

avg_difference = sum(differences) / len(differences)
