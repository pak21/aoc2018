#!/usr/bin/python3

import sys

seen = {0: True}
total = 0

with open(sys.argv[1]) as f:
    changes = [int(x) for x in f]

while True:
    for change in changes:
        total += change
        if total in seen:
            print(total)
            sys.exit(0)
        seen[total] = True
