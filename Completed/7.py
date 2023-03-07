#! /usr/bin/env python3
# Advent of Code 2022 Day 7

from copy import deepcopy
from collections import defaultdict

data = open('7.in').read()
lines = [x for x in data.split("\n")]

dict = defaultdict(int)
path = []
for line in lines:
    words = line.strip().split()
    if words[1] == "cd":
        if words[2] != "..":
            path.append(words[2])
        if words[2] == "..":
            path.pop()
    elif words[1] == "ls":
        continue
    elif words[0] == "dir":
        continue
    else:
        for i in range(len(path)+1):
            newval = dict[str("/".join(path[:i]))] + int(words[0])
            dict.update({str("/".join(path[:i])): newval})

totUnderThou = 0
for k, v in dict.items():
    if v <= 100000:
        totUnderThou += v
print("part 1:", totUnderThou)

# part 2:
size = dict["/"]
spaceneeded = -40000000 + dict["/"]
print("space needed:", spaceneeded)
for k, v in dict.items():
    if v >= spaceneeded:
        if v < size:
            size = v
print("part 2:",size)


# One Reddit Guy Solution
# from collections import defaultdict
# from itertools import accumulate

# dirs = defaultdict(int)

# for line in open(0).read().splitlines():
#     match line.split():
#         case "$", "cd", "/":
#             path = ["/"]
#         case "$", "cd", "..":
#             path.pop()
#         case "$", "cd", dir:
#             path.append(dir + "/")
#         case "$" | "dir", *_:
#             continue
#         case size, _:
#             for p in accumulate(path):
#                 dirs[p] += int(size)

# print(sum(size for size in dirs.values() if size <= 100_000))
# print(min(size for size in dirs.values() if size >= dirs["/"] - 40_000_000))