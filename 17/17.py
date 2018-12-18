#!/usr/bin/python3

import collections
import re
import sys

pattern = re.compile(r'(.)=(\d+), .=(\d+)\.\.(\d+)')

mine = collections.defaultdict(lambda: collections.defaultdict(lambda: '.'))

with open(sys.argv[1]) as f:
    parsed = [pattern.match(line).groups() for line in f]

for line in parsed:
    if line[0] == 'x':
        for y in range(int(line[2]), int(line[3]) + 1):
            mine[y][int(line[1])] = '#'
    else:
        for x in range(int(line[2]), int(line[3]) + 1):
            mine[int(line[1])][x] = '#'

miny = min(mine)
maxy = max(mine)
minx = min([min(row) for row in mine.values()])
maxx = max([max(row) for row in mine.values()])

def check_direction(water, direction):
    next_position = (water[0], water[1] + direction)
    atnext = mine[next_position[0]][next_position[1]]
    if atnext == '#' or atnext == '~':
        return next_position[1]
    below = (next_position[0] + 1, water[1])
    atbelow = mine[below[0]][below[1]]
    if atbelow != '#' and atbelow != '~':
        return -next_position[1]
    return check_direction(next_position, direction)

spout = (0, 500)
active = set()
active.add(spout)
while True:
    toadd = set()
    toremove = set()
    for water in active:
        down = (water[0] + 1, water[1])
        atdown = mine[down[0]][down[1]]
        if atdown == '.':
            if down[0] <= maxy:
                toadd.add(down)
            mine[down[0]][down[1]] = '|'
        elif atdown == '#' or atdown == '~':
            left_constraint = check_direction(water, -1)
            right_constraint = check_direction(water, 1)
            if left_constraint > 0 and right_constraint > 0:
                for x in range(left_constraint + 1, right_constraint):
                    mine[water[0]][x] = '~'
                toremove.add(water)
            else:
                if left_constraint < 0: left_constraint = -left_constraint
                if right_constraint < 0: right_constraint = -right_constraint
                for x in range(left_constraint + 1, right_constraint):
                    mine[water[0]][x] = '|'
                if water[0] <= maxy:
                    if (water[0], left_constraint + 1) not in active:
                        toadd.add((water[0], left_constraint + 1))
                    if (water[0], right_constraint - 1) not in active:
                        toadd.add((water[0], right_constraint - 1))
    active |= toadd
    active -= toremove

    if not toadd and not toremove:
        break

tildes = 0
bars = 0
for y in range(miny, maxy + 1):
    row = mine[y]
    for c in row.values():
        if c == '~':
            tildes += 1
        elif c == '|':
            bars += 1
print(tildes, tildes + bars)
