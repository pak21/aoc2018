#!/usr/bin/python3

import math
import matplotlib.pyplot as plt
from operator import itemgetter
import random
import re
import sys

pattern = re.compile(r'pos=<([-\d]+),([-\d]+),([-\d]+)>, r=(\d+)')

with open(sys.argv[1]) as f:
    bots = [[int(x) for x in pattern.match(line).groups()] for line in f]

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
    
def score(p):
    return sum([distance(bot, p) <= bot[3] for bot in bots])

random.seed(42)

mean = (0, 0, 0)
for b in bots:
    mean = (mean[0] + b[0], mean[1] + b[1], mean[2] + b[2])
mean = (int(mean[0] / len(bots)), int(mean[1] / len(bots)), int(mean[2] / len(bots)))

a = (44889071, 20785698, 42944032) # 922
a = (44890224, 20909341, 42819236) # 922
a = (44909360, 20754849, 42954592) # 922

#a = (0, 0, 0)
#a = (43753564, 21333722, 41417541) # 895
#a = (44861187, 20774372, 42983235) # 917
#a = (45096517, 20655249, 41585290) # 919
sa = score(a)

INITIAL_STEP = 1e6
STEPS = 100000

step = INITIAL_STEP
for i in range(STEPS):
    b = [*a]
    b[0] += int(step * (random.random() - 0.5))
    b[1] += int(step * (random.random() - 0.5))
    b[2] += int(step * (random.random() - 0.5))
    sb = score(b)
    print(step, a, b, sa, sb)
    if sb >= sa:
        a = b
        sa = sb
    step *= 0.9999

print(a, a[0] + a[1] + a[2])

sys.exit(0)

answer = None
for dx in range(-20, 21):
    for dy in range(-20, 21):
        for dz in range(-20, 21):
            b = (a[0] + dx, a[1] + dy, a[2] + dz)
            sb = score(b)
            if sb == sa:
                x = b[0] + b[1] + b[2]
                if answer == None or x < answer:
                    answer = x
                    print(b, answer)
