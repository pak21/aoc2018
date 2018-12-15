#!/usr/bin/python3

import collections
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
                units.append([x, y, row[x] == 'E', False, 200])
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

def find_enemies(this, units):
    enemies = []
    for u in units:
        if u[2] != this[2] and (abs(u[0] - this[0]) + abs(u[1] - this[1])) == 1:
            enemies.append(u)
    return enemies

def prune_states(states):
    foo = collections.defaultdict(list)
    for state in states:
        foo[state[1]].append(state[0])
    bar = [(min(v), k) for k, v in foo.items()]
    return bar

with open(sys.argv[1]) as f:
    grid = [list(r.rstrip()) for r in f.readlines()]

units = create_units(grid)

rounds = 0

while True:
    for u in units:
        u[3] = False

    while True:
        units = [u for u in units if u[4] > 0]
        units.sort(key=itemgetter(1, 0))
        locations = set([(u[0], u[1]) for u in units])

        canmove = [unit for unit in units if not unit[3]]
        if not canmove:
            break

        tomove = canmove[0]

        if not find_enemies(tomove, units):
            targets = find_targets(units, tomove)
            if not targets:
                totalhp = sum([u[4] for u in units])
                print(rounds * totalhp)
                sys.exit(0)
            
            adjacents = find_adjacents(targets)

            t = (tomove[0], tomove[1])
            previous_locations = set(t)
            states = [('', t)]
            allends = None
            while states and not allends:
                newstates = []
                for state in states:
                    newstates += generate_paths(state[0], state[1], previous_locations)
                states = prune_states(newstates)
                previous_locations |= set([s[1] for s in states])
                allends = set([s[1] for s in states if s[1] in adjacents])

            if allends:
                chosen = min(allends, key=itemgetter(1, 0))
                chosen_states = [s for s in states if s[1] == chosen]
                best_state = sorted(chosen_states, key=itemgetter(0))[0]
                chosen_direction = int(best_state[0][0])

                tomove[0] += directions[chosen_direction][0]
                tomove[1] += directions[chosen_direction][1]

        tomove[3] = True

        enemies = find_enemies(tomove, units)
        if enemies:
            toattack = min(enemies, key=itemgetter(4))
            toattack[4] -= 3

    rounds += 1
