#!/usr/bin/python3

import collections
import heapq
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
    if key not in regions:
        regions[key] = get_cell((key[0], key[1])) % 3
    return regions[key]

with open(sys.argv[1]) as f:
    depth = int(f.readline().split()[1])
    tx, ty = [int(i) for i in f.readline().split()[1].split(',')]

grid = {}
regions = {}

print('Part 1: {}'.format(sum([get_region_type((x, y)) for y in range(ty + 1) for x in range(tx + 1)])))

def try_news(new):
    for e in range(3):
        new2 = (*new, e)
        if get_region_type(current) == new2[2] or get_region_type(new2) == new2[2]:
            continue
        new_distance = distances[current] + (8 if current[2] != new2[2] else 1)
        if new_distance < distances[new2]:
            distances[new2] = new_distance
            heapq.heappush(active, (new_distance, new2))

start = (0, 0, 1)
target = (tx, ty, 1)

distances = collections.defaultdict(lambda: 8 * (tx + ty))
distances[start] = 0
active = []
current = start

while current != target:
    if current[0] > 0:
        try_news((current[0] - 1, current[1]))
    if current[1] > 0:
        try_news((current[0], current[1] - 1))
    try_news((current[0] + 1, current[1]))
    try_news((current[0], current[1] + 1))

    current = heapq.heappop(active)[1]

print('Part 2: {}'.format(distances[target]))
