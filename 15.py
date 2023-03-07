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

#  and (x,row) not in pairs.values()

# data = open("15.in").read().strip()
# lines = [x for x in data.split('\n')]

# S = set()
# B = set()
# sum_d = 0
# for line in lines:
#     words = line.split()
#     sx,sy = words[2],words[3]
#     bx,by = words[8],words[9]
#     sx = int(sx[2:-1])
#     sy = int(sy[2:-1])
#     bx = int(bx[2:-1])
#     by = int(by[2:])
#     d = abs(sx-bx) + abs(sy-by)
#     sum_d += d
#     S.add((sx,sy,d))
#     B.add((bx,by))

# def valid(x,y,S):
#     for (sx,sy,d) in S:
#         dxy = abs(x-sx)+abs(y-sy)
#         if dxy<=d:
#             return False
#     return True

# p1 = 0
# for x in range(-int(1e7),int(1e7)):
#     y = int(2e6)
#     if not valid(x,y,S) and (x,y) not in B:
#         p1 += 1
# print(p1)