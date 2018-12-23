#!/usr/bin/python3

from operator import itemgetter
import re
import sys

pattern = re.compile(r'pos=<([-\d]+),([-\d]+),([-\d]+)>, r=(\d+)')

with open(sys.argv[1]) as f:
    bots = [[int(x) for x in pattern.match(line).groups()] for line in f]

strongest = max(bots, key=itemgetter(3))

count = 0
for bot in bots:
    d = abs(bot[0] - strongest[0]) + abs(bot[1] - strongest[1]) + abs(bot[2] - strongest[2])
    if d <= strongest[3]:
        count += 1

print(count)
