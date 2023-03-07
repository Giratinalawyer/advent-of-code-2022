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

#nthistle's solution; important parts are how lambda functions work, declaring global variables, and the dx/dy approach
# import string
# from aoc_tools import *

# with open("input.txt") as f:
#     s = f.read().strip()

# global rope
# rope = [[0,0] for _ in range(10)]

# sign = lambda x : 1 if x > 0 else (
#     -1 if x < 0 else 0)

# # i >= 1
# def update(i):
#     global rope
#     hx,hy = rope[i-1]
#     tx,ty = rope[i]
#     dx = tx-hx
#     dy = ty-hy
#     if dx == 0 or dy == 0:
#         if abs(dx) >= 2:
#             rope[i][0] -= sign(dx)
#         if abs(dy) >= 2:
#             rope[i][1] -= sign(dy)
#     elif (abs(dx),abs(dy)) != (1,1):
#         rope[i][0] -= sign(dx)
#         rope[i][1] -= sign(dy)


# m = {
#     "U":(0,1),
#     "D":(0,-1),
#     "R":(1,0),
#     "L":(-1,0)
# }

# p = set()

# for x in s.split("\n"):
#     dr,n = x.split(" ")
#     n = int(n)
#     p.add(tuple(rope[-1]))
#     for _ in range(n):
#         dx,dy = m[dr]
#         rope[0][0] += dx
#         rope[0][1] += dy
#         for i in range(1,10):
#             update(i)
#         p.add(tuple(rope[-1]))

# print(len(p))