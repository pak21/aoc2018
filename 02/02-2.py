#!/usr/bin/python3

import sys

with open(sys.argv[1]) as f:
    lines = list(f)

for i in range(0, len(lines)):
    line1 = lines[i]
    for j in range(0, i):
        line2 = lines[j]
        diffs = sum([line1[k] != line2[k] for k in range(0, len(line1))])
        if diffs <= 1:
            shared = ''.join([line1[k] for k in range(0, len(line1)) if line1[k] == line2[k]])
            print(shared)
