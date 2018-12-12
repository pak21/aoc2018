#!/usr/bin/python3

import re
import sys

initialpattern = re.compile(r'initial state: (.*)')
rulepattern = re.compile(r'(.....) => (.)')
remove = re.compile(r'^\.*(#.*#)\.*$')

with open(sys.argv[1]) as f:
    state = initialpattern.match(f.readline()).group(1)
    f.readline()
    rules = dict([rulepattern.match(line).groups() for line in f])

zerooffset = 0
for i in range(20):
    zerooffset += state.index('#') - 2
    state = '....' + remove.sub(r'\1', state) + '....'
    newstate = ''.join([rules[state[j:j+5]] for j in range(len(state)-4)])
    state = newstate

print(sum([i + zerooffset for i, c in enumerate(state) if c == '#']))
