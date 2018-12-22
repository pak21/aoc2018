#!/usr/bin/python3

import collections
from operator import itemgetter
import sys

def dump(grid):
    for row in grid:
        print(''.join([['.', '=', '|'][c] for c in row]))

with open(sys.argv[1]) as f:
    depth = int(f.readline().split()[1])
    tx, ty = [int(i) for i in f.readline().split()[1].split(',')]

grid = [None] * (ty + 1)

for y in range(ty+1):
    grid[y] = [None] * (tx + 1)
    grid[y][0] = (48271 * y + depth) % 20183

for x in range(tx+1):
    grid[0][x] = (16807 * x + depth) % 20183

for y in range(1, ty+1):
    for x in range(1, tx+1):
        grid[y][x] = ((grid[y-1][x] * grid[y][x-1]) + depth) % 20183

grid[ty][tx] = 0

for y in range(ty+1):
    for x in range(tx+1):
        grid[y][x] = grid[y][x] % 3

print('Part 1: {}'.format(sum([sum(row) for row in grid])))

start = (0, 0, True, False)

distances = {start: 0}
current = start

visited = set()

def try_new(new):
    new_distance = distances[current] + 1 # TODO
    if new not in distances or new_distance < distances[new]:
        distances[new] = new_distance

def get_next(distances, visited):
    unvisited = [(k, v) for k, v in distances.items() if k not in visited]
    return min(unvisited, key=itemgetter(1))[0]

while True:
    if current[0] > 0:
        try_new((current[0] - 1, current[1], current[2], current[3]))
    if current[1] > 0:
        try_new((current[0], current[1] - 1, current[2], current[3]))
    try_new((current[0] + 1, current[1], current[2], current[3]))
    try_new((current[0], current[1] + 1, current[2], current[3]))

    visited.add(current)

    current = get_next(distances, visited)

    if (tx, ty, True, False) in distances:
        break

print(distances)
