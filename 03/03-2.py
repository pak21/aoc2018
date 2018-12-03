#!/usr/bin/python3

import collections
import sys

claims = collections.defaultdict(lambda: collections.defaultdict(lambda: []))
count = 0

with open(sys.argv[1]) as f:
    for line in f:
        claim, _, anchor, size = line.split()
        claim = int(claim[1:])
        left, top = anchor.split(',')
        left = int(left)
        top = int(top[:-1])
        width, height = map(int, size.split('x'))
        for x in range(left, left + width):
            for y in range(top, top + height):
                claims[x][y].append(claim)
        count += 1

good = set(range(1, count + 1))

for x in claims.values():
    for y in x.values():
        if (len(y) > 1):
            for z in y:
                if z in good:
                    good.remove(z)

print(good)
