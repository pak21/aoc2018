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
    events = [(m, e) for _, m, e in sorted([(lambda t: (t[0], int(t[1]), t[2]))(pattern.match(line).groups()) for line in f], key=lambda t: t[0])]

eventswithlast = [(l, m, e) for (l, _), (m, e) in zip([(None, None)] + events, events)]

guard = None
for event in eventswithlast:
    lastminute, minute, eventstring = event
    if eventstring == 'wakes up': 
        asleep[guard] += minute - lastminute
        for i in range(lastminute, minute):
            whenasleep[guard][i] += 1
    elif eventstring == 'falls asleep':
        pass
    else:
        guard = int(guardpattern.match(eventstring).group(1))

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
