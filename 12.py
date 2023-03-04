#! /usr/bin/env python3

# Advent of Code 2022 Day _

import string
from copy import deepcopy
import numpy as np
from collections import defaultdict

data = open('12.in').read()
chunks = [x for x in data.split('\n')]
m = []

for s in chunks:
    lines = s.split("\n")
    mn = int(lines[0].split()[1][:-1])
    st = [int(lines[1].split()[i][0:2]) for i in range(2, len(lines[1].split()))]
    op = lines[2][len("  Operation: new = "):]
    tst = int(lines[3].split()[-1])
    tr = int(lines[4].split()[-1])
    fl = int(lines[5].split()[-1])
    m.append((mn,st,op,tst,tr,fl))