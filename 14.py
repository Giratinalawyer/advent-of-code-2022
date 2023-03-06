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

for m in range(height*2):
    filled.add((m+500,height+2))
    filled.add((-m+500,height+2))

def sanding(cave: set, pt: int):
    sand = deepcopy(cave)
    i = 0
    while True:
        space = True
        sand.add((500,0))
        locx = 500
        locy = 0
        turns = 0
        while space:
            turns += 1
            if pt == 1 and locy >= height:
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
            if pt == 2:
                if locy == 0:
                    break
        if pt == 1 and locy >= height:
            break
        i += 1
        if pt == 2 and locy == 0:
            break
    return i,sand

# Visualization stuff:

#a[] is purely for visualization
a = []
for i in range(height+4):
    a.append([])
    for j in range(width+1):
        a[i].append("*")

for (j,i) in filled:
    if i == 0:
        a[i-min(heights)][j-min(widths)+1] = "S"
    elif -1 < i-min(heights) < len(a) and -1 < j-min(widths)+1 < len(a[0]):
        a[i-min(heights)][j-min(widths)+1] = "#"
for i,j in enumerate(a):
    print("".join(j))

print("\n")

# more visualization stuff
for (m,n) in sanding(filled,1)[1]:
    if not(m,n) in filled:
        a[n-min(heights)][m-min(widths)+1] = "O"
for p,q in enumerate(a):
    print("".join(q))


print("Answers:")
print("part 1:", sanding(filled,1)[0])
print("part 2:", sanding(filled,2)[0])

