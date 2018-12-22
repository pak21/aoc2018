#!/usr/bin/python3

import collections
from operator import itemgetter
import sys

def calculate_cell(key):
    if key[0] == 0:
        geologic_index = key[1] * 48271
    elif key[1] == 0:
        geologic_index = key[0] * 16807
    elif key[0] == tx and key[1] == ty:
        geologic_index = 0
    else:
        geologic_index = get_cell((key[0] - 1, key[1])) * get_cell((key[0], key[1] - 1))

    erosion_level = (geologic_index + depth) % 20183
    return erosion_level

def get_cell(key):
    if key not in grid:
        grid[key] = calculate_cell(key)
    
    return grid[key]

def get_region_type(key):
    return get_cell((key[0], key[1])) % 3

with open(sys.argv[1]) as f:
    depth = int(f.readline().split()[1])
    tx, ty = [int(i) for i in f.readline().split()[1].split(',')]

grid = {}

print('Part 1: {}'.format(sum([get_region_type((x, y)) for y in range(ty + 1) for x in range(tx + 1)])))

start = (0, 0, True, False)

distances = {start: 0}
active = {start: 0}
current = start

visited = set()

def is_valid(region_type, state):
    if region_type == 0:
        # Rocky, must have one or the other equipped
        return state[2] or state[3]
    if region_type == 1:
        # Wet, must not have the torch equipped
        return not state[2]
    if region_type == 2:
        # Narrow, must not have climbing gear equipped
        return not state[3]

def try_new(new):
    old_region_type = get_region_type(current)
    new_region_type = get_region_type(new)
    if not is_valid(old_region_type, new):
        return
    if not is_valid(new_region_type, new):
        return
    distance = 1
    if current[2] != new[2] or current[3] != new[3]:
        distance += 7 
    new_distance = distances[current] + distance
    if new not in distances or new_distance < distances[new]:
        distances[new] = new_distance
        active[new] = new_distance

def try_news(new):
    try_new((new[0], new[1], False, False))
    try_new((new[0], new[1], False, True))
    try_new((new[0], new[1], True, False))

def get_next(distances, visited):
    unvisited = [(k, v) for k, v in active.items()]
    return min(unvisited, key=itemgetter(1))[0]

while (tx, ty, True, False) not in visited:
    if current[0] > 0:
        try_news((current[0] - 1, current[1], current[2], current[3]))
    if current[1] > 0:
        try_news((current[0], current[1] - 1, current[2], current[3]))
    if current[0] < 80:
        try_news((current[0] + 1, current[1], current[2], current[3]))
    try_news((current[0], current[1] + 1, current[2], current[3]))

    visited.add(current)
    if len(distances) % 1000 == 0:
        print(len(distances), current[1])

    current = get_next(distances, visited)
    del active[current]

print('Part 2: {}'.format(distances[(tx, ty, True, False)]))
