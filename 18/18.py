#!/usr/bin/python3

import collections
import re
import sys

def dump():
    for row in grid:
        print(''.join(row))

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
    grid = [[c for c in row.rstrip()] for row in f]

generations = 0
while generations < 1000:
    newgrid = [None] * len(grid)
    for y in range(len(grid)):
        row = grid[y]
        newgrid[y] = [None] * len(row)
        for x in range(len(row)):
            newgrid[y][x] = evolve(y, x)
    grid = newgrid
    generations += 1
    print(generations, score())

dump()
print(score())
