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
time = 0

workers = 5
extra_time = 60

worker_finish_at = [None] * workers
worker_doing = [None] * workers
being_worked = set()
while True:
    for i in range(0, workers):
        if worker_finish_at[i] == time:
            finished = worker_doing[i]
            answer += finished
            print('Time {}: worker {} finished step {}'.format(time, i, finished))
            worker_doing[i] = None
            worker_finish_at[i] = None

            del dependencies[finished]
            for k in dependencies.keys():
                dependencies[k].discard(finished)

            print('Time {}: {} jobs left to do'.format(time, len(dependencies)))

            if not len(dependencies):
                print(answer)
                sys.exit(0)

    for i in range(0, workers):
        if worker_doing[i] == None:
            canrun = sorted([k for k, v in dependencies.items() if not len(v) and k not in being_worked])
            if canrun:
                willrun = canrun[0]
                worker_finish_at[i] = time + extra_time + ord(willrun) - 64
                worker_doing[i] = willrun
                being_worked.add(willrun)
                print('Time {}: worker {} doing {}, will finish at {}'.format(time, i, worker_doing[i], worker_finish_at[i]))
    time += 1
