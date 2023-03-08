#! /usr/bin/env python3

# Advent of Code 2022 Day 16
# Tried using PyPy on this one, looks like it did speed stuff up when needed to do subset checking at beginning of solve() for part 1
# but it didn't seem to like numpy or regex, so would want to solve that if trying to use it in the future
#should learn re.findall too

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]
import string
from copy import deepcopy
import math
# import numpy as np
from collections import defaultdict, deque
from functools import cmp_to_key
import time
# from aoc_tools import *

start = time.time()
data = open('16.in').read().strip()
lines = [x for x in data.split('\n')]

flows = {}
tunnels = {}
for entry in lines:
    line = entry.split(" ")
    valve = line[1]
    rate = int(line[4][5:-1])
    leads = tuple([x.strip(",").strip("\r") for x in line[9:]])
    flows[valve] = rate
    tunnels[valve] = leads
print(flows)
print(tunnels)

def solve(flow, tunnel): #pretty much all taken from Cancamussa AKA carrdelling (https://github.com/carrdelling/AdventOfCode2022/blob/main/day16/silver.py)
    # similar philosophy to my approach's attempt, just obviously implemented much more correctly.
    states = [(1, 'AA',0,("zzz",))]
    seen = {}
    seen_valves = {}
    best = 0

    while len(states) > 0:
        current = states.pop()
        time, where, score, opened_s = current
        opened = {x for x in opened_s}
        
        if seen.get((time,where), -1) >= score and opened.issubset(seen_valves.get((time,where),-1)): # apparently dict[] will raise keyerror if key does not exist, but .get() returns second arg if that happens (so should generally use .get)
            continue
        seen[(time,where)] = score
        seen_valves[(time,where)] = opened

        if time == 30:
            best = max(best,score)
            continue
    
        # if we open the valve here
        if flow[where] > 0 and where not in opened:
            opened.add(where)
            new_score = score + sum(flow.get(where, 0) for where in opened)
            new_state = (time + 1, where, new_score, tuple(opened))

            states.append(new_state)
            opened.discard(where)
    
        #if we don't open a valve here
        new_score = score + sum(flow.get(where,0) for where in opened)
        for option in tunnel.get(where):
            new_state = (time + 1, option, new_score, tuple(opened))
            states.append(new_state)
    
    return best

print(solve(flows,tunnels))
end = time.time()
print(end-start)



# Your first attempt for part 1: - main problems are runtime, and also probably horrible recursive function semantics
# def get_paths(path, time): #recursive function 
# # for checking all 30-valve paths
#     # print(path)
#     if time == 31:
#         # print(path)
#         global bestpres
#         if bestpres == 0:
#             bestpres = pres(path)
#         elif pres(path) > bestpres:
#             bestpres = pres(path)
#             print(bestpres)
#         return bestpres
#     newlist = path[:]
#     newlist.append(" ")
#     # print(newlist)
#     if valves[path[-1]][0] != 0:
#         unopened = True
#         for i in range(len(path)):
#             if path[i-1] == path[-1] and path[i] == path[-1]:
#                 unopened = False
#         if unopened:
#             newlist[-1] = path[-1]
#             get_paths(newlist, time +1)
#     for lead in valves[path[-1]][1]:
#         newlist[-1] = lead
#         get_paths(newlist, time + 1)

# def pres(route):
#     assert(len(route)) == 31
#     pressure = 0
#     tunnels = route[1:]
#     prev = None
#     for i, choice in enumerate(tunnels):
#         if prev == None:
#             prev = choice
#             continue
#         else:
#             if choice == prev:
#                 pressure += valves[choice][0] * (29 - i)
#         prev = choice
#     return(pressure)

# print(pres(['AA', 'DD', 'DD', 'CC', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'AA', 'DD', 'AA', 'DD', 'AA', 'II', 'JJ', 'II', 'JJ', 'JJ', 'II', 'AA', 'DD']))
# print(pres(['AA','DD','DD','CC','BB','BB','AA','II','JJ','JJ','II','AA','DD','EE','FF','GG','HH','HH','GG','FF','EE','EE','DD','CC','CC','DD','CC','DD','CC','DD','CC']))
# curr = 'AA'
# bestpres = 0
# start = ['AA']
# get_paths(start, 1)
# print(bestpres)