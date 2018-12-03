#!/usr/bin/python3

import collections
import sys

claims = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))

with open(sys.argv[1]) as f:
    for line in f:
        _, _, anchor, size = line.split()
        left, top = anchor.split(',')
        left = int(left)
        top = int(top[:-1])
        width, height = map(int, size.split('x'))
        for x in range(left, left + width):
            for y in range(top, top + height):
                claims[x][y] += 1

count = 0

for x in claims.values():
    for y in x.values():
        if (y > 1):
            count += 1

print(count)
