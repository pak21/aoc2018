#!/usr/bin/python3

import re
import string
import sys

pattern = re.compile('Step (.) must be finished before step (.) can begin\.')

dependencies = {c: set() for c in string.ascii_uppercase}

with open(sys.argv[1]) as f:
    for line in f:
        before, after = pattern.match(line).groups()
        dependencies[after].add(before)

answer = ''
while dependencies:
    willrun = sorted([k for k, v in dependencies.items() if not len(v)])[0]
    answer += willrun
    del dependencies[willrun]
    for v in dependencies.values():
        v.discard(willrun)

print(answer)
