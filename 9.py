#! /usr/bin/env python3

# Advent of Code 2022 Day 9

from copy import deepcopy
import numpy as np
from collections import defaultdict

data = open('9.in').read().strip()
lines = [x for x in data.split('\n')]

n = 10 #n = 2 for part 1, n = 10 for part 2
a = [[0,0] for x in range(n)] # initialize rope knots; a[0] = head, a[n-1] = tail
visits = set()

for line in lines:
    d, amt = line.split()
    for j in range(int(amt)):
        visits.add(tuple(a[n-1]))
        # print(d, "step", i)
        if d == "R":
            a[0][1] += 1
        elif d == "L":
            a[0][1] -= 1
        elif d == "D":
            a[0][0] -= 1
        elif d == "U":
            a[0][0] += 1
        for i in range(0,n-1):
            if abs(a[i][0]-a[i+1][0]) < 2 and abs(a[i][1]-a[i+1][1]) < 2:
                continue
            elif a[i][0] == a[i+1][0]:
                if a[i][1] - a[i+1][1] > 1:
                    a[i+1][1] += 1
                elif a[i][1] - a[i+1][1] < -1:
                    a[i+1][1] -= 1
            elif a[i][1] == a[i+1][1]:
                if a[i][0] - a[i+1][0] > 1:
                    a[i+1][0] += 1
                elif a[i][0] - a[i+1][0] < -1:
                    a[i+1][0] -= 1
            else:
                if a[i+1][0] < a[i][0]:
                    a[i+1][0] += 1
                else:
                    a[i+1][0] -= 1
                if a[i+1][1] < a[i][1]:
                    a[i+1][1] += 1
                else:
                    a[i+1][1] -= 1
visits.add(tuple(a[i+1]))
print("total unique visits by tail for %i rope knots:" % (n), len(visits))

# not bad. 40 minutes for part 1, 15 for part 2?