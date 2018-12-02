#!/usr/bin/python3

import collections
import sys

count2 = 0
count3 = 0

with open(sys.argv[1]) as f:
    for line in f:
        counts = collections.defaultdict(lambda: 0)
        for c in line.rstrip():
            counts[c] += 1
        if 2 in counts.values():
            count2 += 1
        if 3 in counts.values():
            count3 += 1

print(count2, count3, count2 * count3)
