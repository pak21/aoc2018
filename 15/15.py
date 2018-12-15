#!/usr/bin/python3

from operator import itemgetter
import sys

directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]

def valid_position(p):
    return grid[p[1]][p[0]] == '.' and p not in locations

def create_units(grid):
    units = []
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            if row[x] == 'E' or row[x] == 'G':
                units.append([x, y, row[x] == 'E', False])
                row[x] = '.'
    return units

def find_targets(units, unit):
    return [t for t in units if t[2] != unit[2]]

def find_adjacents(targets):
    adjacents = set()
    for t in targets:
        for d in directions:
            new = (t[0] + d[0], t[1] + d[1])
            if not valid_position(new):
                continue
            adjacents.add(new)
    return adjacents

def generate_paths(path, end, previous):
    newpaths = []
    for i in range(len(directions)):
        direction = directions[i]
        new = (end[0] + direction[0], end[1] + direction[1])
        if valid_position(new) and new not in previous:
            newpath = path + str(i)
            newpaths.append((newpath, new))
    return newpaths

def next_to_enemy(this, units):
    for u in units:
        if u[2] != this[2] and (abs(u[0] - this[0]) + abs(u[1] - this[1])) == 1:
            return True
    return False

def dump(grid, units):
    picture = [[c for c in row] for row in grid]
    for unit in units:
        y = unit[1]
        x = unit[0]
        picture[y][x] = 'E' if unit[2] else 'G'
    for row in picture:
        print(''.join(row))

with open(sys.argv[1]) as f:
    grid = [list(r.rstrip()) for r in f.readlines()]

units = create_units(grid)

while True:
    dump(grid, units)
    for u in units:
        u[3] = False

    while True:

        units.sort(key=itemgetter(1, 0))
        locations = set([(u[0], u[1]) for u in units])

        canmove = [unit for unit in units if unit[3] == False]
        if not canmove:
            break

        tomove = canmove[0]
        print('To move', tomove)

        if next_to_enemy(tomove, units):
            print('Not moving, next to enemy')
            tomove[3] = True
            continue

        targets = find_targets(units, tomove)
    #    print('Targets', targets)
        adjacents = find_adjacents(targets)
    #    print('Adjacents', adjacents)

        t = (tomove[0], tomove[1])
        previous_locations = set()
        previous_locations.add(t)
        states = [('', t)]
        done = False
        while states and not done:
            newstates = []
            for state in states:
                newstates += generate_paths(state[0], state[1], previous_locations)
            states = newstates
            previous_locations |= set([s[1] for s in states])
            allends = set([s[1] for s in states if s[1] in adjacents])
            if allends:
                done = True

        if allends:
            chosen = min(allends, key=itemgetter(1, 0))
            chosen_states = [s for s in states if s[1] == chosen]
            best_state = sorted(chosen_states, key=itemgetter(0))[0]
            chosen_direction = int(best_state[0][0])

            tomove[0] += directions[chosen_direction][0]
            tomove[1] += directions[chosen_direction][1]
            print('Now at', tomove)

        tomove[3] = True
