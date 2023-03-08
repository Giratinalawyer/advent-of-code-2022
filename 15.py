#! /usr/bin/env python3

# Advent of Code 2022 Day 15
# learn z3 constrain solver at some point, and pypy
dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]
import string
from copy import deepcopy
import math
import numpy as np
from collections import defaultdict, deque
from functools import cmp_to_key
import time
from aoc_tools import *

start = time.time()
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

bds = dict() # beacon distances
for k in pairs.keys():
    bds[k] = taxicab(k,pairs[k])

beacset = set()
for v in pairs.values():
    beacset.add(v)

pos = 0
timesetup = time.time()
print("time leading up to part 1 loop:", timesetup - start)
for x in range(x_min - max_d, x_max+max_d+1, 1): #includes going further in dirxns that edgemost beacons/sensors!
#would be nice if this loop ran faster
    further = 0
    for k in pairs.keys():
        if taxicab((x,row),k) <= bds[k]:
            further = 1
            break
    if further and (x,row) not in beacset:
        pos += 1
print("part 1:",pos)
time1 = time.time()
print("time for part 1:", time1-timesetup)

#part 2:
found = False
for k in pairs.keys(): #damn. 3.7 seconds!
    #this loop was taken from Jpaulson after mine was taking forever.
    for dx in range(bds[k]+2):
        dy = bds[k]-dx+1
        for signx,signy in dirs:
            x = k[0]+(dx*signx)
            y = k[1]+(dy*signy)
            if not(0 <= x <=4000000 and 0 <= y <= 4000000):
                continue
            valid = True
            for k in pairs.keys():
                dxy = taxicab((x,y),k)
                if dxy <=bds[k]:
                    valid = False
                    break
            if valid:
                found = True
                print("part 2:", 4000000*x+y)
                break
        if found:
            break
    if found:
        break

#old loop involved adding all edge members to a set and then removing those that were not valid. I guess that takes a while to do compared to this format.

time2 = time.time()
print("time for part 2:", time2-time1)