#! /usr/bin/env python3
# Advent of Code 2022 Day 8

from copy import deepcopy
import numpy as np

data = open('8.in').read()
lines = [x for x in data.split('/n')] #note - you fucked the /n up, should be \n. Fixed this on day 9.

words =[]
for line in lines:
    words = line.strip().split()

# words = ['30373', '25512', '65332', '33549', '35390']

peak = len(words)

for i in range(peak):
    words[i] = list(words[i])

words = np.array(words)
words = words.astype(np.intc)
wordsrot = words.transpose()

count = 0
for i in range(peak):
    for j in range(len(words[i])):
        if i == 0 or j == 0 or i == (peak -1) or j == (peak-1):
            count += 1
        elif np.amax(words[i][0:j], axis = 0) < words[i][j]:
            count += 1
        elif np.amax(words[i][j+1:peak], axis = 0) < words[i][j]:
            count += 1
        elif np.amax(wordsrot[j][0:i], axis = 0) < words[i][j]:
            count += 1
        elif np.amax(wordsrot[j][i+1:peak], axis = 0) < words[i][j]:
            count += 1

#part 2
currmax = 0
for i in range(peak):
    for j in range(len(words[i])):
        a = j
        if i == 0 or j == 0 or i == (peak-1) or j == (peak-1):
            a = 0
            continue
        for p in range(j-1,-1,-1):
            if words[i][p] >= words[i][j]:
                a = j-p
                break
        b = peak-j-1
        for p in range(j+1,peak):
            if words[i][p] >= words[i][j]:
                b = p-j
                break
        c = i
        for p in range(i-1,-1,-1):
            if wordsrot[j][p] >= wordsrot[j][i]:
                c = i - p
                break
        d = peak-i-1
        for p in range(i+1,peak):
            if wordsrot[j][p] >= wordsrot[j][i]:
                d = p - i
                break
        if currmax < a*b*c*d:
            currmax = a*b*c*d

print("part 1:", count)
print("part 2:", currmax)

#Paulson's code:
# import sys
# from collections import defaultdict
# infile = sys.argv[1] if len(sys.argv)>1 else '8.in'
# data = open(infile).read().strip()
# lines = [x for x in data.split('\n')]

# G = []
# for line in lines:
#     row = line
#     G.append(row)

# DIR = [(-1,0),(0,1),(1,0),(0,-1)]
# R = len(G)
# C = len(G[0])

# p1 = 0
# for r in range(R):
#     for c in range(C):
#         vis = False
#         for (dr,dc) in DIR:
#             rr = r
#             cc = c
#             ok = True
#             while True:
#                 rr += dr
#                 cc += dc
#                 if not (0<=rr<R and 0<=cc<C):
#                     break
#                 if G[rr][cc] >= G[r][c]:
#                     ok = False
#             if ok:
#                 vis = True
#         if vis:
#             p1 += 1
# print(p1)

# p2 = 0
# for r in range(R):
#     for c in range(C):
#         score = 1
#         for (dr,dc) in DIR:
#             dist = 1
#             rr = r+dr
#             cc = c+dc
#             while True:
#                 if not (0<=rr<R and 0<=cc<C):
#                     dist -= 1
#                     break
#                 if G[rr][cc]>=G[r][c]:
#                     break
#                 dist += 1
#                 rr += dr
#                 cc += dc
#             score *= dist
#         p2 = max(p2, score)
# print(p2)

#nthistle code
# import string
# from aoc_tools import *

# with open("input.txt") as f:
#     s = f.read().strip()

# g = [[int(y) for y in x] for x in s.split("\n")]
# n = len(g)
# m = len(g[0])

# vis = set()
# for i in range(n):
#     for j in range(m):
#         isviz = False
#         for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
#             ni = i + dx
#             nj = j + dy
#             v = True
#             while ni in range(n) and nj in range(m):
#                 if g[ni][nj] >= g[i][j]:
#                     v = False
#                     break
#                 ni += dx
#                 nj += dy
#             if v:
#                 isviz = True
#                 break
#         if isviz:
#             vis.add((i, j))

# print(len(vis))

# r = 0

# for i in range(n):
#     for j in range(m):
#         vd = []
#         for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
#             ni = i + dx
#             nj = j + dy
#             c = 0
#             v = True
#             while ni in range(n) and nj in range(m):
#                 if g[ni][nj] >= g[i][j]:
#                     v = False
#                     break
#                 ni += dx
#                 nj += dy
#                 c += 1
#             vd.append(c + (1 if ni in range(n) and nj in range(m) else 0))
#         r = max(r, vd[0]*vd[1]*vd[2]*vd[3])

# print(r)