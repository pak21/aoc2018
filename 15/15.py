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
                units.append([x, y, row[x] == 'E', False, 200])
                row[x] = '.'
    return units

def find_adjacents(targets):
    adjacents = set()
    for t in targets:
        for d in directions:
            new = (t[0] + d[0], t[1] + d[1])
            if not valid_position(new):
                continue
            adjacents.add(new)
    return adjacents

def generate_paths(newstates, position, path, previous):
    for i in range(len(directions)):
        direction = directions[i]
        new = (position[0] + direction[0], position[1] + direction[1])
        if valid_position(new) and new not in previous:
            newpath = path + str(i)
            if new not in newstates or newpath < newstates[new]:
                newstates[new] = newpath

def find_enemies(this, units):
    return [u for u in units if u[2] != this[2] and (abs(u[0] - this[0]) + abs(u[1] - this[1])) == 1]

with open(sys.argv[1]) as f:
    grid = [list(r) for r in f.readlines()]

units = create_units(grid)

rounds = 0

while True:
    for u in units:
        u[3] = False

    while True:
        units = [unit for unit in units if unit[4] > 0]

        units.sort(key=itemgetter(1, 0))
        locations = set([(unit[0], unit[1]) for unit in units])

        canmove = [unit for unit in units if not unit[3]]
        if not canmove:
            break
        tomove = canmove[0]

        if not find_enemies(tomove, units):
            targets = [target for target in units if target[2] != tomove[2]]
            if not targets:
                totalhp = sum([unit[4] for unit in units])
                print(rounds * totalhp)
                sys.exit(0)
            
            adjacents = find_adjacents(targets)

            previous_locations = set()
            states = {(tomove[0], tomove[1]): ''}
            allends = None
            while states and not allends:
                previous_locations |= set(states)
                newstates = {}
                for position, path in states.items():
                    generate_paths(newstates, position, path, previous_locations)
                states = newstates
                allends = [s for s in states if s in adjacents]

            if allends:
                chosen = min(allends, key=itemgetter(1, 0))
                chosen_direction = int(states[chosen][0])

                tomove[0] += directions[chosen_direction][0]
                tomove[1] += directions[chosen_direction][1]

        tomove[3] = True

        enemies = find_enemies(tomove, units)
        if enemies:
            toattack = min(enemies, key=itemgetter(4))
            toattack[4] -= 3

    rounds += 1
