#!/usr/bin/python3

import collections
import sys

with open(sys.argv[1]) as f:
    points = [[int(x) for x in line.split(',')] for line in f]

edges = collections.defaultdict(list)
for i, p1 in enumerate(points):
    for j in range(i):
        if sum([abs(p1[k] - points[j][k]) for k in range(len(p1))]) <= 3:
            edges[i].append(j)
            edges[j].append(i)

n = 0
constellations = [None] * len(points)
for i in range(len(points)):
    if constellations[i] != None:
        continue
    constellations[i] = n
    active = [i]
    while active:
        a = active.pop()
        for e in edges[a]:
            if constellations[e] == None:
                constellations[e] = n
                active.append(e)
    n += 1

print(n)
