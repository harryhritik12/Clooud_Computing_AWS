#!/usr/bin/env python

import sys

# Initialize variables to hold the current candidate and points
current_candidate = None
points = []

for line in sys.stdin:
    candidate, point = line.strip().split('\t')
    point = tuple(map(float, point.split(',')))

    if current_candidate == candidate:
        points.append(point)
    else:
        # Calculate the new candidate point by averaging the points
        if current_candidate:
            new_candidate = (
                sum(p[0] for p in points) / len(points),
                sum(p[1] for p in points) / len(points)
            )
            print(f"{current_candidate}\t{new_candidate[0]},{new_candidate[1]}")
        current_candidate = candidate
        points = [point]

# Output the last candidate
if current_candidate:
    new_candidate = (
        sum(p[0] for p in points) / len(points),
        sum(p[1] for p in points) / len(points)  # Corrected typo here
    )
    print(f"{current_candidate}\t{new_candidate[0]},{new_candidate[1]}")
