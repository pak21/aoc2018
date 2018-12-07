#!/usr/bin/python3

import collections
import datetime
import operator
import re
import sys

pattern = re.compile('Step (.) must be finished before step (.) can begin\.')

dependencies = collections.defaultdict(set)

with open(sys.argv[1]) as f:
    for line in f:
        x, y = pattern.match(line).groups()
        dependencies[y].add(x)
        if x not in dependencies:
            dependencies[x] = set()

answer = ''
try:
    while True:
        canrun = sorted([k for k, v in dependencies.items() if not len(v)])
        willrun = canrun[0]

        answer += willrun
        del dependencies[willrun]
        for k in dependencies.keys():
            dependencies[k].discard(willrun)
except:
    print(answer)
