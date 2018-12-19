#!/usr/bin/python3

import collections
import re
import sys

TIME_TO_STABILISE = 1000
TARGET_TIME = 1000000000

def evolve(y, x):
    old = grid[y][x]
    o = 0
    t = 0
    l = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny >= len(grid):
                continue
            if nx < 0 or nx >= len(grid[0]):
                continue
            lookat = grid[ny][nx]
            if lookat == '.':
                o += 1
            elif lookat == '|':
                t += 1
            elif lookat == '#':
                l += 1
    new = old
    if old == '.' and t >= 3:
        new = '|'
    if old == '|' and l >= 3:
        new = '#'
    if old == '#':
        if l >= 1 and t >= 1:
            pass
        else:
            new = '.'
    return new

def score():
    t = 0
    l = 0
    for row in grid:
        for column in row:
            if column == '|':
                t += 1
            elif column == '#':
                l += 1
    return t * l

with open(sys.argv[1]) as f:
    grid = [list(row.rstrip()) for row in f]

generations = 0
scores = []
while True:
    newgrid = [None] * len(grid)
    for y in range(len(grid)):
        row = grid[y]
        newgrid[y] = [None] * len(row)
        for x in range(len(row)):
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
