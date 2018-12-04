#!/usr/bin/python3

import collections
import datetime
import operator
import re
import sys

pattern = re.compile(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)')
guardpattern = re.compile(r'Guard #(\d+) begins shift')

events = []
asleep = collections.defaultdict(lambda: 0)
whenasleep = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))

with open(sys.argv[1]) as f:
    for line in f:
        matches = pattern.match(line).groups()
        year, month, day, hour, minute, eventstring = matches
        eventtime = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        if eventstring == 'wakes up':
            event = -1
        elif eventstring == 'falls asleep':
            event = -2
        else:
            event = int(guardpattern.match(eventstring).group(1))
        events.append((eventtime, event))

events = sorted(events, key=lambda x: x[0])

guard = None
lastminute = None
for event in events:
    eventtime, eventtype = event
    if eventtype > 0:
        guard = event[1]
    if eventtime.hour == 23:
        eventtime += datetime.timedelta(minutes=60-eventtime.minute)

    if eventtype == -1:
        #print('Guard {} asleep from {} to {}'.format(guard, lastminute, eventtime.minute))
        asleep[guard] += eventtime.minute - lastminute
        for i in range(lastminute, eventtime.minute):
            whenasleep[guard][i] += 1
    elif eventtype == -2:
        #print('Guard {} awake from {} to {}'.format(guard, lastminute, eventtime.minute))
        pass

    lastminute = eventtime.minute

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
