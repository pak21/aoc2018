#!/usr/bin/python3

import collections
import sys

directions = {
        'E': (1, 0),
        'N': (0, 1),
        'W': (-1, 0),
        'S': (0, -1)
        }

stack = []
with open(sys.argv[1]) as f:
    for regex in f:
        regex = regex.strip()

        current = (0, 0)
        stack = []
        valid_moves = collections.defaultdict(set)
        for c in list(regex):
            if c == '^' or c == '$':
                pass
            elif c in directions:
                d = directions[c]
                new = (current[0] + d[0], current[1] + d[1])
                valid_moves[current].add(new)
                current = new
            elif c == '(':
                stack.append(current)
            elif c == '|':
                current = stack[-1]
            elif c == ')':
                current = stack.pop()

        moves = 1
        start = (0, 0)
        seen_locations = set()
        current_locations = set()
        seen_locations.add(start)
        current_locations.add(start)
        far_away = 0

        while current_locations:
            new_locations = set()
            for l in current_locations:
                for m in valid_moves[l]:
                    if m not in seen_locations:
                        if moves >= 1000:
                            far_away += 1
                        new_locations.add(m)
                        seen_locations.add(m)
            moves += 1
            current_locations = new_locations

        print('{}: Part 1: {}, Part 2: {}'.format(regex, moves - 2, far_away))
