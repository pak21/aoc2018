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
        row[i] = [abs(x - c[0]) + abs(y - c[1]) for c in coords]
        mindist = min(row[i])
        row[i] = [j - mindist for j in row[i]]
        zeros = sum([j == 0 for j in row[i]])
        if zeros == 1:
            row[i] = row[i].index(0)
        else:
            row[i] = -1
    counts[y - miny] = collections.Counter(row)

print(counts)

for counter in counts:
    for k, v in counter.items():
        foo[k] += v

print(foo)

infinites = set()

for y in range(maxy - miny + 1):
    infinites.add(distances[y][0])
    infinites.add(distances[y][maxx - minx])

for x in range(maxx - minx + 1):
    infinites.add(distances[0][x])
    infinites.add(distances[maxy - miny][x])

print(infinites)

for i in infinites:
    del foo[i]

print(foo)

bar = max(foo.items(), key=operator.itemgetter(1))

print(bar)
