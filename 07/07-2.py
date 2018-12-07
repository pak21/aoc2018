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

time = 0

worker_count = 5
extra_time = 60

workers = [(None, None)] * worker_count
being_worked = set()

while dependencies:
    for i in range(worker_count):
        if workers[i][1] == time:
            finished = workers[i][0]
            workers[i] = (None, None)

            del dependencies[finished]
            for v in dependencies.values():
                v.discard(finished)

    for i in range(worker_count):
        if workers[i][0] == None:
            canrun = sorted([k for k, v in dependencies.items() if not len(v) and k not in being_worked])
            if canrun:
                willrun = canrun[0]
                workers[i] = (willrun, time + extra_time + ord(willrun) - 64)
                being_worked.add(willrun)

    time += 1

print(time - 1)
