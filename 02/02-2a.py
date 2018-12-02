#!/usr/bin/python3

import sys

with open(sys.argv[1]) as f:
   lines = list(f)

print([
        ''.join([p[0] for p in match])
        for match
        in filter(
            lambda match: len(match) >= len(lines[0]) - 1,
            [
                list(filter(lambda p: p[0] == p[1], pair))
                for pair in
                [
                    zip(lines[i], lines[j])
                    for i in range(0, len(lines))
                    for j in range(0, i)
                ]
            ]
        )
    ])
