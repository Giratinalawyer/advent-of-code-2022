#! /usr/bin/env python3

# Advent of Code 2022 Day 14

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
import string
from copy import deepcopy
import math
import numpy as np
from collections import defaultdict, deque
from functools import cmp_to_key

data = open('14.in').read().strip()
lines = [x for x in data.split('\n')]

