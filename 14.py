#! /usr/bin/env python3

# Advent of Code 2022 Day 14
# still need to learn zip, map, lambda, walrus operator
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
    cvcp = deepcopy(cave)
    i = 0
    while True:
        sand = (500,0)
        while True:
            if (sand[0],sand[1]+1) not in cvcp:
                sand = (sand[0],sand[1]+1)
            elif (sand[0]-1,sand[1]+1) not in cvcp:
                sand = (sand[0]-1,sand[1]+1)
            elif (sand[0]+1,sand[1]+1) not in cvcp:
                sand = (sand[0]+1,sand[1]+1)
            else:
                break
        cvcp.add(sand)
        if pt == 1 and sand[1] > height:
            break
        i += 1
        if sand == (500,0):
            break
    return i,cvcp

# if (pt == 1 and sand[1] >= height) or (pt == 2 and sand[1] == 0):
#     break

# Visualization stuff:
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

for (m,n) in sanding(filled,1)[1]:
    if not(m,n) in filled:
        a[n-min(heights)][m-min(widths)+1] = "O"
for p,q in enumerate(a):
    print("".join(q))
#_________________________________

print("Answers:")
print("part 1:", sanding(filled,1)[0])
print("now for part 2:")
print("part 2:", sanding(filled,2)[0])


#JPaulson's solution - after improvements, yours is basically his
# R = set()
# for line in lines:
#     prev = None
#     for point in line.split('->'):
#         x,y = point.split(',')
#         x,y = int(x),int(y)
#         if prev is not None:
#             dx = x-prev[0]
#             dy = y-prev[1]
#             len_ = max(abs(dx),abs(dy))
#             for i in range(len_+1):
#                 xx = prev[0]+i*(1 if dx>0 else (-1 if dx<0 else 0))
#                 yy = prev[1]+i*(1 if dy>0 else (-1 if dy<0 else 0))
#                 R.add((xx,yy))
#         prev = (x,y)

# floor = 2+max(r[1] for r in R)
# #print(floor)
# lo_x = min(r[0] for r in R)-2000
# hi_x = max(r[0] for r in R)+2000
# for x in range(lo_x, hi_x):
#     R.add((x,floor))

# did_p1 = False
# for t in range(1000000):
#     rock = (500,0)
#     while True:
#         if rock[1]+1>=floor and (not did_p1):
#             did_p1 = True
#             print(t)
#         if (rock[0],rock[1]+1) not in R:
#             rock = (rock[0],rock[1]+1)
#         elif (rock[0]-1,rock[1]+1) not in R:
#             rock = (rock[0]-1, rock[1]+1)
#         elif (rock[0]+1, rock[1]+1) not in R:
#             rock = (rock[0]+1, rock[1]+1)
#         else:
#             break
#     if rock == (500,0):
#         print(t+1)
#         break
#     R.add(rock)


# nthistle soln:
# import string
# from collections import defaultdict
# #from aoc_tools import *
# dirs = [(0,1),(1,0),(0,-1),(-1,0)]

# with open(r"C:\Users\Neil\Documents\AOC2022\day14\input.txt") as f:
#     s = f.read().strip()
# print("\n".join(x[:60] for x in s.split("\n")[:6]))

# s = s.split("\n")
# s = [[tuple(nums(x)) for x in line.split(" -> ")] for line in s]
# # added for pypy
# #s = [[tuple(map(int,x.split(","))) for x in line.split(" -> ")] for line in s]

# sand = (500,0)

# # 0 -> air
# # 1 -> solid
# # 2 -> solid sand
# grid = defaultdict(lambda : 0)
# for line in s:
#     for (ax,ay),(bx,by) in zip(line,line[1:]):
#         dx = bx-ax
#         if dx != 0:
#             dx = dx // abs(dx)
#         dy = by-ay
#         if dy != 0:
#             dy = dy // abs(dy)
#         while (ax,ay) != (bx,by):
#             grid[ax,ay] = 1
#             ax += dx
#             ay += dy
#         grid[ax,ay] = 1

# maxy = max(y for x,y in grid)

# for x in range(-1000,1000):
#     grid[x,maxy+2] = 1

# part = 2

# sx,sy = sand
# while True:
#     blocked = True
#     for dx,dy in ((0,1),(-1,1),(1,1)):
#         if grid[(sx+dx,sy+dy)] == 0:
#             sx += dx
#             sy += dy
#             blocked = False
#             break
#     if part == 1 and sy > maxy:
#         break
#     if blocked:
#         grid[sx,sy] = 2
#         if (sx,sy) == sand:
#             break
#         sx,sy = sand

# print(sum(1 for v in grid.values() if v == 2))