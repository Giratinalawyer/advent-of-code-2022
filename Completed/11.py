#! /usr/bin/env python3

# Advent of Code 2022 Day _

import string
from copy import deepcopy
import numpy as np
from collections import defaultdict

data = open('11.in').read()
monkeys = [x for x in data.split('\n\n')]
m = []

for s in monkeys:
    lines = s.split("\n")
    mn = int(lines[0].split()[1][:-1])
    st = [int(lines[1].split()[i][0:2]) for i in range(2, len(lines[1].split()))]
    op = lines[2][len("  Operation: new = "):]
    tst = int(lines[3].split()[-1])
    tr = int(lines[4].split()[-1])
    fl = int(lines[5].split()[-1])
    m.append((mn,st,op,tst,tr,fl))
# print(monkeys[0])
# print(m)

mitems = [[x for x in st] for _,st,_,_,_,_ in m]
mit2 = deepcopy(mitems)

lcm = 1
for mnk in m:
    lcm = lcm * mnk[3]
print(lcm)
counts = [0 for _ in m]
rds = 20 #change number of rounds here; 20 for part 1, 10000 for part 2

for _ in range(rds):
    for j in range(len(m)):
        for item in mit2[j]:
            old = item
            new = eval(m[j][2])
            counts[j] += 1
            if rds == 20:
                new = new//3
            else: new = new % lcm
            if new % (m[j][3]) == 0:
                mit2[m[j][4]].append(new)
            else: mit2[m[j][5]].append(new)
        mit2[j].clear()

sort = sorted(counts)
print(sort)
part = 2 if rds == 10000 else 1
print("part %i:" % (part), sort[-1]*sort[-2])

#Thistle soln https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/izr4r7a/?utm_source=share&utm_medium=web2x&context=3
# (I used his as a guide while writing this anyway, so of course I'm pretty much the same. Still, educational!)

# with open("input.txt") as f:
#     s = f.read().strip()
# print("\n".join(x[:60] for x in s.split("\n")[:10]))


# s = s.split("\n\n")

# m = []
# N = 1
# for x in s:
#     lns = x.split("\n")
#     mn = nums(lns[0])[0]
#     st = nums(lns[1])
#     op = lns[2][len("  Operation: "):]
#     tst = nums(lns[3])[0]
#     iftrue = nums(lns[4])[0]
#     iffalse = nums(lns[5])[0]
#     N *= tst
#     m.append((mn, st, op, tst, iftrue, iffalse))

# mitems = [[x for x in st] for _,st,_,_,_,_ in m]
# counts = [0 for _ in m]

# # reproduced part 1 code
# for _ in range(20):
#     for i in range(len(m)):
#         mnk = m[i]
#         for item in mitems[i]:
#             counts[i] += 1
#             old = item
#             new = eval(mnk[2][5:])
#             if new % mnk[3] == 0:
#                 mitems[mnk[4]].append(new)
#             else:
#                 mitems[mnk[5]].append(new)
#         mitems[i].clear()
        
# counts.sort()
# print(counts[-1] * counts[-2])

# mitems = [[x for x in st] for _,st,_,_,_,_ in m]
# counts = [0 for _ in m]

# for _ in range(10000):
#     for i in range(len(m)):
#         mnk = m[i]
#         for item in mitems[i]:
#             counts[i] += 1
#             old = item
#             new = eval(mnk[2][5:])
#             new %= N
#             if new % mnk[3] == 0:
#                 mitems[mnk[4]].append(new)
#             else:
#                 mitems[mnk[5]].append(new)
#         mitems[i].clear()


# counts.sort()
# print(counts[-1] * counts[-2])