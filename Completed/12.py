#! /usr/bin/env python3

# Advent of Code 2022 Day 12
# Note!: must delete last line of 12.in if you want this to work. Jonathan Paulson's solution *does* work with the blank line. Somehow.


import string
from copy import deepcopy
import numpy as np
from collections import defaultdict, deque

data = open('12.in').read().strip()
m = [x for x in data.split('\n')] #map

visited = {} #all interior visited locations
layer = {} #current outermost locations accessed
nbrs = {} #boundary of visited locations which has *not* been added yet
top = {} #entire map

colLen = [a[0] for a in m] #column length of map

for i in range(len(m[0])):  #creates dictionary with 2-tuples and letter values of positions
    for j in range(len(colLen)):
        top[(j,i)] = m[j][i]

for key,value in top.items(): #Gets positions of start and end
    if value == "S":
        start = key
    if value == "E":
        end = key

def addneighb1 (pt: tuple): #adds all valid neighbors for the current position
    for neighb in ((pt[0]+1, pt[1]),(pt[0]-1, pt[1]),(pt[0], pt[1]-1),(pt[0], pt[1]+1)):
        if not(neighb in visited) and neighb in top:
            if (pt == start and ord(top[neighb]) < ord("c")) or (ord(top[pt]) > ord("x") and top[neighb] == "E") or (ord(top[pt]) >= ord(top[neighb])-1):
                nbrs[neighb] = top[neighb]

def addneighb2 (pt: tuple): #adds all valid neighbors for the current position...going in reverse from peak.
    for neighb in ((pt[0]+1, pt[1]),(pt[0]-1, pt[1]),(pt[0], pt[1]-1),(pt[0], pt[1]+1)):
        if not(neighb in visited) and neighb in top:
            if (pt == end and ord(top[neighb]) > ord("x")) or (ord(top[pt]) <= ord(top[neighb])+1):
                nbrs[neighb] = top[neighb]

steps = 0
aset = {}
aset[start] = top[start] # use this for part 1 - just S
# for key,value in top.items(): # can use this for part 2 - all points where the altitude is "a"
#     if value == "a":          # see further down for solution to part 2 that runs faster
#         aset[key] = value

for point in aset:
    layer.clear()
    nbrs.clear()
    visited.clear()
    layer[point] = aset[point]
    i = 0
    while not((end) in layer.keys()): #add neighbors for all current layer points and iterate until the goal is in layer
        for curr in layer:
            addneighb1(curr)
            visited[curr] = layer[curr]
        layer.clear()
        layer = deepcopy(nbrs)
        nbrs.clear()
        i += 1
        if steps != 0:
            if i > steps:
                break #don't bother continuing for part 2 if we've already taken more steps than our fastest route
    if i < steps or steps == 0:
        steps = i #update steps if new route length is faster.

print("part 1:", steps)

aset.clear()
aset[end] = top[end]

# Part 2 BFS: - this approach starts at the peak, and works backwards to the closest "a".
# Uses a different neighbor function (neighb2) to account for needing to go down elevation by at most 1.
for point in aset:
    layer.clear()
    nbrs.clear()
    visited.clear()
    layer[point] = aset[point]
    i = 0
    while not("a" in layer.values()): #add neighbors for all current layer points and iterate until the goal is in layer
        for curr in layer:
            addneighb2(curr)
            visited[curr] = layer[curr]
        layer.clear()
        layer = deepcopy(nbrs)
        nbrs.clear()
        i += 1
print("part 2:", i)


# Paulson solution:

# #!/usr/bin/python3
# import sys
# import math
# from copy import deepcopy
# from collections import defaultdict, deque
# infile = sys.argv[1] if len(sys.argv)>1 else '12.in'
# data = open(infile).read().strip()
# lines = [x for x in data.split('\n')]

# G = []
# for line in lines:
#     G.append(line)
# R = len(G)
# C = len(G[0])

# E = [[0 for _ in range(C)] for _ in range(R)]
# for r in range(R):
#     for c in range(C):
#         if G[r][c]=='S':
#             E[r][c] = 1
#         elif G[r][c] == 'E':
#             E[r][c] = 26
#         else:
#             E[r][c] = ord(G[r][c])-ord('a')+1

# def bfs(part):
#     Q = deque()
#     for r in range(R):
#         for c in range(C):
#             if (part==1 and G[r][c]=='S') or (part==2 and E[r][c] == 1):
#                 Q.append(((r,c), 0))

#     S = set()
#     while Q:
#         (r,c),d = Q.popleft()
#         if (r,c) in S:
#             continue
#         S.add((r,c))
#         if G[r][c]=='E':
#             return d
#         for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
#             rr = r+dr
#             cc = c+dc
#             if 0<=rr<R and 0<=cc<C and E[rr][cc]<=1+E[r][c]:
#                 Q.append(((rr,cc),d+1))
# print(bfs(1))
# print(bfs(2))

#nthistle's solution
# import string
# from aoc_tools import *
# dirs = [(0,1),(1,0),(0,-1),(-1,0)]

# with open("input.txt") as f:
#     s = f.read().strip()
            
# best = 10000
# for sx2 in range(41):
#     for sy2 in range(81):
#         #print("\n".join(x[:60] for x in s.split("\n")[:10]))

#         g = [list(x) for x in s.split("\n")]
#         n = len(g)
#         m = len(g[0])

#         sx,sy = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "S"][0]
#         tx,ty = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "E"][0]

#         g[sx][sy] = "a"
#         g[tx][ty] = "z"

#         if g[sx2][sy2] != "a":
#             continue

#         g = [[ord(c) - ord("a") for c in r] for r in g]

#         from collections import deque

#         dst = defaultdict(lambda : 1000000)
#         dst[sx2,sy2] = 0

#         q = deque([(sx2,sy2)])
#         ans = 100000
#         while len(q) > 0:
#             cx,cy = q.popleft()
#             if (cx,cy) == (tx,ty):
#                 ans = dst[tx,ty]
#                 if (sx2,sy2) == (sx,sy):
#                     print(ans)
#                 break
#             for dx,dy in dirs:
#                 nx,ny = cx+dx,cy+dy
#                 if nx in range(n) and ny in range(m):
#                     if g[cx][cy] >= g[nx][ny] - 1:
#                         ndst = dst[cx,cy] + 1
#                         if ndst < dst[nx,ny]:
#                             q.append((nx,ny))
#                             dst[nx,ny] = ndst
#         best = min(best,ans)
# print(best)