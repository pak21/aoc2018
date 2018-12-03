#!/usr/bin/python3

import collections
import re
import sys

claims = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))

pattern = re.compile(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)')

with open(sys.argv[1]) as f:
    for line in f:
        matches = pattern.match(line).groups
        left, top, width, height = map(int, matches(0))
        for x in range(left, left + width):
            for y in range(top, top + height):
                claims[x][y] += 1

print(sum(map(lambda row: len(list(filter(lambda i: i > 1, row.values()))), claims.values())))
