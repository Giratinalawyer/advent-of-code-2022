#! /usr/bin/env python3

# Advent of Code 2022 Day 14

d1,d2,d3 = [(0,1),(-1,1),(1,1)]
import string
from copy import deepcopy
import math
import numpy as np
from collections import defaultdict, deque
from functools import cmp_to_key

data = open('14.in').read().strip()
lines = [x for x in data.split('\n')]

filled = set()

for line in lines: #ripped from Jpaulson's solution and carefully analyzed after frustration with own rock filling loop.
    prev = None
    for point in line.split('->'):
        x,y = point.split(',')
        x,y = int(x),int(y)
        if prev is not None:
            dx = x-prev[0]
            dy = y-prev[1]
            len_ = max(abs(dx),abs(dy))
            for i in range(len_+1):
                xx = prev[0]+i*(1 if dx>0 else (-1 if dx<0 else 0))
                yy = prev[1]+i*(1 if dy>0 else (-1 if dy<0 else 0))
                filled.add((xx,yy))
        prev = (x,y)

filled.add((500,0))
heights = [x[1] for x in filled]
heights.append(0)
widths = [x[0] for x in filled]
width = max(widths) - min(widths)+2
height = max(heights)

sand = deepcopy(filled)
i = 0

space = True
while True:
    space = True
    sand.add((500,0))
    locx = 500
    locy = 0
    turns = 0
    while space:
        turns += 1
        if locy >= max(heights):
            break
        elif not((locx,locy + 1) in sand):
            sand.add((locx,locy+1))
            sand.remove((locx,locy))
            locy = locy + 1
        elif not((locx-1,locy+1) in sand):
            sand.add((locx-1,locy+1))
            sand.remove((locx,locy))
            locx = locx -1
            locy = locy +1
        elif not((locx+1,locy+1) in sand):
            sand.add((locx+1,locy+1))
            sand.remove((locx,locy))
            locx, locy = locx +1, locy +1
        else:
            sand.add((locx,locy))
            space = False
    if locy >= max(heights):
        break
    i += 1

print("Part 1:",i)

# part 2:
for m in range(height*2):
    filled.add((m+500,height+2))
    filled.add((-m+500,height+2))

sand2 = deepcopy(filled)
i = 0
while True:
    space = True
    sand2.add((500,0))
    locx = 500
    locy = 0
    turns = 0
    while space:
        turns += 1
        if not((locx,locy + 1) in sand2):
            sand2.add((locx,locy+1))
            sand2.remove((locx,locy))
            locy = locy + 1
        elif not((locx-1,locy+1) in sand2):
            sand2.add((locx-1,locy+1))
            sand2.remove((locx,locy))
            locx = locx -1
            locy = locy +1
        elif not((locx+1,locy+1) in sand2):
            sand2.add((locx+1,locy+1))
            sand2.remove((locx,locy))
            locx, locy = locx +1, locy +1
        else:
            sand2.add((locx,locy))
            space = False
        if locy == 0:
            break
    i += 1
    if locy == 0:
        break

for (p,j) in sand2:
    if j < 5:
        print((p,j))
print(i)


# Visualization stuff:

# #a[] is purely for visualization
# a = []
# for i in range(height+1):
#     a.append([])
#     for j in range(width+1):
#         a[i].append("*")

# for (j,i) in filled:
#     if i == 0:
#         a[i-min(heights)][j-min(widths)+1] = "S"
#     else:
#         a[i-min(heights)][j-min(widths)+1] = "#"
# for i,j in enumerate(a):
#     print("".join(j))

# print("\n")

#more visualization stuff
# for (m,n) in sand:
#     if not(m,n) in filled:
#         a[n-min(heights)][m-min(widths)+1] = "O"
# for p,q in enumerate(a):
#     print("".join(q))

# print("locy:",locy)