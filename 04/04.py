#!/usr/bin/python3

from collections import defaultdict
from operator import itemgetter
import re
import sys

pattern = re.compile(r'\[(.*:(\d+))\] (.*)')
guardpattern = re.compile(r'Guard #(\d+) begins shift')

events = []
whenasleep = defaultdict(lambda: defaultdict(lambda: 0))

with open(sys.argv[1]) as f:
    events = [(int(m), e) for _, m, e in sorted([pattern.match(line).groups() for line in f], key=itemgetter(0))]

eventswithlast = [(l, m, e) for (l, _), (m, e) in zip([(None, None)] + events, events)]

guard = None
for event in eventswithlast:
    lastminute, minute, eventstring = event
    if eventstring == 'wakes up': 
        for i in range(lastminute, minute):
            whenasleep[guard][i] += 1
    elif eventstring == 'falls asleep':
        pass
    else:
        guard = int(guardpattern.match(eventstring).group(1))

# Part 1

mostasleep, _ = max([(k, sum(v.values())) for k, v in whenasleep.items()], key=itemgetter(1))
howlongasleep, _ = max(whenasleep[mostasleep].items(), key=itemgetter(1))
print('{} * {} = {}'.format(mostasleep, howlongasleep, mostasleep * howlongasleep))

# Part 2

mostminutesasleepbyguard = [(k, *max(v.items(), key=itemgetter(1))) for k, v in whenasleep.items()]
mostasleep, howlongasleep, _ = max(mostminutesasleepbyguard, key=itemgetter(2))
print('{} * {} = {}'.format(mostasleep, howlongasleep, mostasleep * howlongasleep))
