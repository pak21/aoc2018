#!/usr/bin/python3

import collections
import datetime
import operator
import re
import sys

pattern = re.compile(r'\[(.*:(\d+))\] (.*)')
guardpattern = re.compile(r'Guard #(\d+) begins shift')

events = []
asleep = collections.defaultdict(lambda: 0)
whenasleep = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))

with open(sys.argv[1]) as f:
    for line in f:
        matches = pattern.match(line).groups()
        events.append((wholedate, int(minute), eventstring))

events = sorted(events, key=lambda x: x[0])

guard = None
lastminute = None
for event in events:
    wholedate, minute, eventstring = event
    if eventstring == 'wakes up': 
        asleep[guard] += minute - lastminute
        for i in range(lastminute, minute):
            whenasleep[guard][i] += 1
    elif eventstring == 'falls asleep':
        pass
    else:
        guard = int(guardpattern.match(eventstring).group(1))

    lastminute = minute

# Part 1

mostasleep = max(asleep.items(), key=operator.itemgetter(1))[0]
mostasleepdata = whenasleep[mostasleep]
amountasleep = max(mostasleepdata.items(), key=operator.itemgetter(1))[0]

print(mostasleep, amountasleep, mostasleep * amountasleep)

# Part 2

overallmax = -1
for guard, asleepcounts in whenasleep.items():
    for minute, timesasleep in asleepcounts.items():
        if timesasleep > overallmax:
            data = (guard, minute)
            overallmax = timesasleep

print(data, data[0] * data[1])
