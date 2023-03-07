#! /usr/bin/env python3

# Advent of Code 2022 Day 15

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
import string
from copy import deepcopy
import math
import numpy as np
from collections import defaultdict, deque
from functools import cmp_to_key

data = open('15.in').read().strip()
lines = [x for x in data.split('\n')]

pairs = dict()

for line in lines:
    line = line.split(" ")
    sensor = (int(line[2][2:-1]),int(line[3][2:-1]))
    beacon = (int(line[-2][2:-1]),int(line[-1][2:]))
    pairs[sensor] = beacon

x_min = min(min([k[0] for k in pairs.keys()]),min([v[0] for v in pairs.values()]))
x_max = max(max([k[0] for k in pairs.keys()]),max([v[0] for v in pairs.values()]))
y_min = min(min([k[1] for k in pairs.keys()]),min([v[1] for v in pairs.values()]))
y_max = max(max([k[1] for k in pairs.keys()]),max([v[1] for v in pairs.values()]))
print(x_min,x_max,y_min,y_max)
row = 2000000 #change for example input!

def taxicab(src, dest):
    return abs(src[0]-dest[0])+abs(src[1]-dest[1])

max_d = max([taxicab(k,pairs[k]) for k in pairs.keys()])
print("max_d:",max_d)

beacset = set()
for v in pairs.values():
    beacset.add(v)
pos = 0
for x in range(x_min - max_d, x_max+max_d+1, 1): #includes going further in dirxns that edgemost beacons/sensors!
#would be nice if this loop ran faster
    further = 0
    for k in pairs.keys():
        if taxicab((x,row),k) <= taxicab(k,pairs[k]):
            # print((x,row))
            # print("source:",k)
            further = 1
            break
    if further and (x,row) not in beacset:
        pos += 1
print("number of cases:",pos)

#part 2:
ans = ()
for x in range(0,4000001)
    for y in range (0,4000001):
        further = 1
        for k in pairs.keys():
            if taxicab((x,y),k) <= taxicab(k,pairs[k]:
                further = 0
                break
        if further = 0:
            break
    if further and (x,y) not in beacset:
        ans = (x,y)
        break
print(4000000*ans[0] + ans[1])

# will probably need to make this faster. best guess so far is make a set of all tuples which cannot contain a beacon, then check in the range