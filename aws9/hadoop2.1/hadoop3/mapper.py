#!/usr/bin/env python

import sys
import math

# Hardcoded candidate points
candidates = [
    (5.8, 4.0),
    (6.1, 2.8),
    (6.3, 2.7)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if len(values) != 5:
        continue  # Skip invalid lines

    sepallength = float(values[0])
    sepalwidth = float(values[1])

    # Initialize variables to track nearest candidate and minimum distance
    min_distance = float('inf')
    nearest_candidate = None

    # Calculate the distance to each hardcoded candidate
    for candidate in candidates:
        distance = euclidean_distance((sepallength, sepalwidth), candidate)
        if distance < min_distance:
            min_distance = distance
            nearest_candidate = candidate

    # Emit the nearest candidate and the point
    print(f"{nearest_candidate[0]},{nearest_candidate[1]}\t{sepallength},{sepalwidth}")
