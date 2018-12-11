#!/usr/bin/python3

import numpy as np

cells = 300
serial = 2694

def powerlevel(x, y, serial):
    rackid = x + 10
    powerlevel = rackid * y
    powerlevel2 = powerlevel + serial
    powerlevel3 = powerlevel2 * rackid
    hundreds = (powerlevel3 % 1000) // 100
    hundreds2 = hundreds - 5
    return hundreds2

def row(y, serial):
    return [powerlevel(x, y, serial) for x in range(1, cells + 1)]

def grid(serial):
    return [row(y, serial) for y in range(1, cells + 1)]

def sumx(row):
    return [sum(row[x:x+3]) for x in range(0, cells - 2)]

g = grid(serial)
sums = [sumx(row) for row in g]

sumsy = [ [sum(x) for x in zip(*sums[y:y+3])] for y in range(0, cells - 2) ]

maxv = -999999
maxy = None
maxx = None
for y in range(0, cells - 2):
    for x in range(0, cells - 2):
        if sumsy[y][x] > maxv:
            maxy = y
            maxx = x
            maxv = sumsy[y][x]

print(maxx + 1, maxy + 1, maxv)
