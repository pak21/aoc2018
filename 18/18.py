#!/usr/bin/python3

import collections
import sys

TIME_TO_STABILISE = 1000
TARGET_TIME = 1000000000

transitions = {
        '.': lambda seen: '|' if seen['|'] >= 3 else '.',
        '|': lambda seen: '#' if seen['#'] >= 3 else '|',
        '#': lambda seen: '#' if seen['|'] >= 1 and seen['#'] >= 1 else '.'
}

def evolve(y, x):
    seen = collections.defaultdict(int)
    for ny in range(y-1, y+2):
        for nx in range(x-1, x+2):
            if (ny == y and nx == x) or ny < 0 or ny >= len(grid) or nx < 0 or nx >= len(grid[0]):
                continue
            seen[grid[ny][nx]] += 1
    return transitions[grid[y][x]](seen)

def score():
    seen = collections.defaultdict(int)
    for row in grid:
        for column in row:
            seen[column] += 1
    return seen['|'] * seen['#']

with open(sys.argv[1]) as f:
    grid = [list(row.rstrip()) for row in f]

generations = 0
scores = []
while True:
    newgrid = [None] * len(grid)
    for y in range(len(grid)):
        newgrid[y] = [None] * len(grid[0])
        for x in range(len(grid[0])):
            newgrid[y][x] = evolve(y, x)
    grid = newgrid
    generations += 1
    if generations % 100 == 0:
        print('Done {} generations'.format(generations))
    if generations == 10:
        print('Part 1 answer: {}'.format(score()))
    elif generations == TIME_TO_STABILISE:
        scores.append(score())
    elif generations >= TIME_TO_STABILISE:
        s = score()
        scores.append(s)
        if s == scores[0]:
            period = generations - TIME_TO_STABILISE
            offset = (TARGET_TIME - TIME_TO_STABILISE) % period
            print('Part 2 answer: {}'.format(scores[offset]))
            break
