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
seenstates = set()

generations = 0
while True:
    generations += 1
    zerooffset += state.index('#') - 2
    state = '....' + remove.sub(r'\1', state) + '....'

    state = ''.join([rules[state[j:j+5]] for j in range(len(state)-4)])
    score = sum([i + zerooffset for i, c in enumerate(state) if c == '#'])

    if generations == 20:
        print(score)

    if state in seenstates:
        break

    seenstates.add(state)
    lastscore = score

print(score + (score - lastscore) * (50000000000 - generations))
