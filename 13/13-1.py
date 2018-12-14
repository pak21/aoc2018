#!/usr/bin/python3

from operator import itemgetter
import sys

moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
directions = {'>': 0, '^': 1, '<': 2, 'v': 3}
newdir_backslash = [3, 2, 1, 0]
newdir_slash = [1, 0, 3, 2]

with open(sys.argv[1]) as f:
    grid = f.readlines()

carts = []

for y in range(len(grid)):
    row = grid[y]
    for x in range(len(row)):
        if row[x] in directions:
            carts.append([y, x, directions[row[x]], 0])

while True:
    order = sorted(sorted(carts, key=itemgetter(1)), key=itemgetter(0))

    for i in range(len(order)):
        cart = order[i]
        direction = cart[2]
        cart[0] += moves[direction][1]
        cart[1] += moves[direction][0]

        newlocation = grid[cart[0]][cart[1]]
        if newlocation == '\\':
            cart[2] = newdir_backslash[direction]
        elif newlocation == '/':
            cart[2] = newdir_slash[direction]
        elif newlocation == '+':
            if cart[3] == 0:
                dirchange = 1
            elif cart[3] == 1:
                dirchange = 0
            elif cart[3] == 2:
                dirchange = -1
            cart[3] = (cart[3] + 1) % 3
            cart[2] = (cart[2] + dirchange) % 4

        for j in range(len(order)):
            if i == j:
                continue
            other = order[j]
            if cart[0] == other[0] and cart[1] == other[1]:
                print('{},{}'.format(cart[1], cart[0]))
                sys.exit(0)
