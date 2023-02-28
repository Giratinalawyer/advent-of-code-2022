#! /usr/bin/env python3

# Advent of Code 2022 Day 10

from copy import deepcopy
import numpy as np
from collections import defaultdict

data = open('6.in').read()
lines = [x for x in data.split('\n')]
