#! /usr/bin/env python3

# Advent of Code 2022 Day 13

import string
from copy import deepcopy
import math
import numpy as np
from collections import defaultdict, deque
from functools import cmp_to_key

data = open('13.in').read().strip()
pairs = [x for x in data.split('\n\n')]

i = 1
sum = 0
def compare(l, r):
  if isinstance(l, int) and isinstance(r,int):
    if l > r:
      return 0
    elif l < r:
      return 1
    else: return -1
  elif isinstance(l, list) and isinstance(r,list):
      j = 0
      while j < len(l) and j < len(r):
        c = compare(l[j],r[j])
        if c == 1:
          return 1
        if c == 0:
          return 0
        j += 1
      if len(l) < len(r):
        return 1
      elif len(l) > len(r):
        return 0
      else: return -1
  elif isinstance(l, int):
    return compare([l],r)
  else:
    return compare(l, [r])

packets = []
for pair in pairs:
    left, right = pair.split('\n')
    left = eval(left)
    right = eval(right)
    packets.append(left)
    packets.append(right)
    ordbool = compare(left, right)
    if ordbool:
      sum += i
    i += 1

print("part 1:", sum)

#part 2:
packets.append([[2]])
packets.append([[6]])
for j in range(len(packets)):
  for i in range(len(packets)-1):
    if compare(packets[i],packets[i+1]) == 0:
      packets[i], packets[i+1] = packets[i+1], packets[i]

for i in range(len(packets)):
  if packets[i] == [[2]]:
    a = i+1
  if packets[i] == [[6]]:
    b = i+1

print("part 2:", a*b)

#nthistle soln:
# import string
# from aoc_tools import *
# dirs = [(0,1),(1,0),(0,-1),(-1,0)]

# with open("input.txt") as f:
#     s = f.read().strip()
# print("\n".join(x[:60] for x in s.split("\n")[:6]))

# s = s.split("\n\n")
# s2 = []
# for x in s:
#     a,b = x.split("\n")
#     s2.append((eval(a),eval(b)))
# s = s2

# def cmp(a,b): # -1 if a < b, 0 if a = b
#     if type(a) is int and type(b) is int:
#         if a < b:
#             return -1
#         elif a == b:
#             return 0
#         else:
#             return 1
#     elif type(a) is list and type(b) is int:
#         b = [b]
#     elif type(a) is int and type(b) is list:
#         a = [a]

#     n = len(a)
#     m = len(b)
#     for aa, bb in zip(a, b): #zip good to know
#         r = cmp(aa, bb)
#         if r != 0:
#             return r
#     if n < m:
#         return -1
#     elif n == m:
#         return 0
#     else:
#         return 1

# r = 0
# for i,(a,b) in enumerate(s):
#     if cmp(a,b) == -1:
#         r += i + 1
# print(r)

# pkts = []
# for a,b in s:
#     pkts.append(a)
#     pkts.append(b)

# pkts.append([[2]])
# pkts.append([[6]])

# for i in range(len(pkts)):
#     for j in range(len(pkts)-1):
#         if cmp(pkts[j], pkts[j+1]) > 0:
#             pkts[j], pkts[j+1] = pkts[j+1], pkts[j]

# x, y = [i for i in range(len(pkts)) if pkts[i] == [[2]] or pkts[i] == [[6]]]
# print((x + 1) * (y + 1))

#jpaulson soln:
# def compare(p1,p2):
#     if isinstance(p1, int) and isinstance(p2,int):
#         if p1 < p2:
#             return -1
#         elif p1 == p2:
#             return 0
#         else:
#             return 1
#     elif isinstance(p1, list) and isinstance(p2, list):
#         i = 0
#         while i<len(p1) and i<len(p2):
#             c = compare(p1[i], p2[i])
#             if c==-1:
#                 return -1
#             if c==1:
#                 return 1
#             i += 1
#         if i==len(p1) and i<len(p2):
#             return -1
#         elif i==len(p2) and i<len(p1):
#             return 1
#         else:
#             return 0
#     elif isinstance(p1, int) and isinstance(p2, list):
#         return compare([p1], p2)
#     else:
#         return compare(p1, [p2])

# packets = []
# part1 = 0
# for i,group in enumerate(data.split('\n\n')): #enumerate good to know
#     p1,p2 = group.split('\n')
#     p1 = eval(p1)
#     p2 = eval(p2)
#     packets.append(p1)
#     packets.append(p2)
#     if compare(p1, p2)==-1:
#         part1 += 1+i
# print(part1)

# packets.append([[2]])
# packets.append([[6]])
# from functools import cmp_to_key
# packets = sorted(packets, key=cmp_to_key(lambda p1,p2: compare(p1,p2))) # cmp to key good to know
# part2 = 1
# for i,p in enumerate(packets):
#     if p==[[2]] or p==[[6]]:
#         part2 *= i+1
# print(part2)