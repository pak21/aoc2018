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

def sumx(row, size):
    return [sum(row[x:x+size]) for x in range(0, cells - size + 1)]

g = grid(serial)

overallmaxv = -999999
overallmaxy = None
overallmaxx = None
overallmaxsize = None

for size in range(1, 50):
    sums = [sumx(row, size) for row in g]
    sumsy = [ [sum(x) for x in zip(*sums[y:y+size])] for y in range(0, cells - size + 1) ]

    maxv = -999999
    maxy = None
    maxx = None
    for y in range(0, cells - size + 1):
        for x in range(0, cells - size + 1):
            if sumsy[y][x] > maxv:
                maxy = y
                maxx = x
                maxv = sumsy[y][x]

    if maxv > overallmaxv:
        overallmaxy = maxy
        overallmaxx = maxx
        overallmaxv = maxv
        overallmaxsize = size

print(overallmaxx + 1, overallmaxy + 1, overallmaxsize, overallmaxv)
