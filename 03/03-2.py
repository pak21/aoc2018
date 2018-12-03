#!/usr/bin/python3

import collections
import re
import sys

claims = collections.defaultdict(lambda: collections.defaultdict(lambda: []))
count = 0

pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

with open(sys.argv[1]) as f:
    for line in f:
        matches = pattern.match(line).groups
        claim, left, top, width, height = map(int, matches(0))
        for x in range(left, left + width):
            for y in range(top, top + height):
                claims[x][y].append(claim)
        count += 1

bad = set()
for row in claims.values():
    for y in filter(lambda a: len(a) > 1, row.values()):
        bad |= set(y)

print(set(range(1, count + 1)) - bad)
