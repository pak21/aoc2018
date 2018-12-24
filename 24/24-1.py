#!/usr/bin/python3

import re
import sys

pattern = re.compile(r'(\d+) units each with (\d+) hit points (\((immune to (.*); )?weak to (.*)\) )?with an attack that does (\d+) (.*) damage at initiative (\d+)')

immune = []
infection = []

with open(sys.argv[1]) as f:
    for unstripped in f:
        line = unstripped.rstrip()

        if line == 'Immune System:':
            current = immune
        elif line == 'Infection:':
            current = infection
        elif line == '':
            continue
        else:
            match = pattern.match(line)
            if match:
                current.append(line)
            else:
                raise Exception('Unknown line', line)

print(immune)
print()
print(infection)
