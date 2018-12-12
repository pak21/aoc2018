#!/usr/bin/python3

import re
import sys

initialpattern = re.compile(r'initial state: (.*)')
rulepattern = re.compile(r'(.....) => (.)')

leftremove = re.compile(r'^\.*#')
rightremove = re.compile(r'#\.*$')

with open(sys.argv[1]) as f:
    state = initialpattern.match(f.readline()).group(1)
    f.readline()
    rules = dict([rulepattern.match(line).groups() for line in f])

zerooffset = 0

for i in range(20):
    firsthash = state.index('#')
    zerooffset += firsthash - 2
    state = leftremove.sub('#', state)
    state = rightremove.sub('#', state)
    state = '....' + state + '....'

    newstate = ''

    for j in range(2, len(state)-2):
        segment = state[j-2:j+3]
        if segment in rules:
            newstate += rules[segment]
        else:
            newstate += '.'

    state = newstate
    print(state)

total = 0
for i in range(len(state)):
    if state[i] == '#':
        total += i + zerooffset

print(zerooffset)
print(total)
