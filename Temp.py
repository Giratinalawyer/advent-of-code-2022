#! /usr/bin/env python3

# Advent of Code 2022 Day _

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]
import string
from copy import deepcopy
import math
import numpy as np
from collections import defaultdict, deque
from functools import cmp_to_key
import time
from aoc_tools import *

data = open('.in').read().strip()
lines = [x for x in data.split('\n')]

