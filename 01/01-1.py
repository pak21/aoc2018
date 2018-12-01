#!/usr/bin/python3

import sys

with open(sys.argv[1]) as f:
    changes = sum([int(x) for x in f])
    print(changes)
