#!/usr/bin/python3

import collections
import functools
import re
import sys

claims = collections.defaultdict(lambda: collections.defaultdict(lambda: set()))
count = 0

pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

with open(sys.argv[1]) as f:
    for line in f:
        claim, left, top, width, height = map(int, pattern.match(line).groups())
        for x in range(left, left + width):
            for y in range(top, top + height):
                claims[x][y].add(claim)
        count += 1

overlaps = functools.reduce(
        lambda a, b: a | b,
        [cell for row in claims.values() for cell in row.values() if len(cell) > 1])
print(set(range(1, count + 1)) - overlaps)
