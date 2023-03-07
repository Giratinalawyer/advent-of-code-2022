#! /usr/bin/env python3

# Advent of Code 2022 Day 10

from copy import deepcopy
import numpy as np
from collections import defaultdict

data = open('10.in').read()
lines = [x for x in data.split('\n')]

signal = [1]

for line in lines:
    word = line.split()
    if word[0] == "noop":
        if signal == [1]:
            signal.append(1)
        else:
            signal.append(signal[-1])
    elif word[0] == "addx":
        if signal == [1]:
            signal.append(1)
            signal.append(signal[-1]+int(word[1]))
        else:
            signal.append(signal[-1])
            signal.append(signal[-1]+int(word[1]))

sum = 0
for i in range(19,259,40):
    sum += signal[i]*(i+1)
print("part 1", sum)


print("part 2:")
for i in range(0,240):
    if i % 40 == 0 and i > 0:
        print("\n",end="")
    if abs(signal[i] - (i % 40)) < 2:
        print("#", end ="")
    else:
        print(".",end="")
print("\n")

#Paulson solution:
# import sys
# from collections import defaultdict
# infile = sys.argv[1] if len(sys.argv)>1 else '10.in'
# data = open(infile).read().strip()
# lines = [x for x in data.split('\n')]


# G = [['?' for _ in range(40)] for _ in range(6)]
# p1 = 0
# x = 1
# t = 0

# def handle_tick(t, x):
#     global p1
#     global G
#     t1 = t-1
#     G[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
#     if t in [20, 60, 100, 140, 180, 220]:
#         p1 += x*t

# for line in lines:
#     words = line.split()
#     if words[0] == 'noop':
#         t += 1
#         handle_tick(t,x)
#     elif words[0] == 'addx':
#         t += 1
#         handle_tick(t,x)
#         t += 1
#         handle_tick(t,x)
#         x += int(words[1])
# print(p1)
# for r in range(6):
#     print(''.join(G[r]))