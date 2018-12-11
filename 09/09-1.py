#!/usr/bin/python3

import sys

with open(sys.argv[1]) as f:
    for line in f:
        players, marbles = [int(x) for x in line.split()]

        circle = [0]
        position = 0
        scores = [0] * players
        for i in range(1, marbles + 1):
            if i % 23 == 0:
                position = (position - 7) % len(circle)
                scores[i % players] += i + circle[position]
                del circle[position]
            else:
                position = ((position + 1) % len(circle)) + 1
                circle.insert(position, i)

        print(max(scores))
