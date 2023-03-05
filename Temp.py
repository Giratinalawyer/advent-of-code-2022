#! /usr/bin/env python3

# Advent of Code 2022 Day _

import string
from copy import deepcopy
import numpy as np
from collections import defaultdict, deque

data = open('.in').read()
lines = [x for x in data.split('\n')]


# figure out how to stop blank line at end issue: start with this, and maybe nthistle's format of file reading
m = []
with open('12.in', 'r') as file1:
  for line in file1.readlines():
      m.append(line.rstrip())
    #   if trimmed_line: # Don't print blank lines
    #       print(trimmed_line)
print('\n'.join(m))