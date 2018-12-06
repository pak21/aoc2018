#!/usr/bin/python3

import collections
import datetime
import operator
import re
import sys

with open(sys.argv[1]) as f:
    coords = [[int(i) for i in line.split(',')] for line in f]

minx = min([c[0] for c in coords])
maxx = max([c[0] for c in coords])
miny = min([c[1] for c in coords])
maxy = max([c[1] for c in coords])

distances = [[]] * (maxy - miny + 1)
counts = [None] * (maxy - miny + 1)
foo = collections.defaultdict(int)
for y in range(miny, maxy + 1):
    row = [0] * (maxx - minx + 1)
    distances[y - miny] = row
    for x in range(minx, maxx + 1):
        i = x - minx
        row[i] = sum([abs(x - c[0]) + abs(y - c[1]) for c in coords]) < 10000

print(sum([sum(r) for r in distances]))
