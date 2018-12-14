#!/usr/bin/python3

from operator import itemgetter
import sys

moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]
directions = {'>': 0, '^': 1, '<': 2, 'v': 3}

with open(sys.argv[1]) as f:
    grid = f.readlines()

carts = [[y, x, directions[grid[y][x]], 0] for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] in directions]

while True:
    order = sorted(carts, key=itemgetter(1, 0))

    for i in range(len(order)):
        cart = order[i]
        cart[0] += moves[cart[2]][0]
        cart[1] += moves[cart[2]][1]

        newlocation = grid[cart[0]][cart[1]]
        if newlocation == '\\':
            cart[2] = 3 - cart[2]
        elif newlocation == '/':
            cart[2] = (5 - cart[2]) % 4
        elif newlocation == '+':
            cart[2] = (cart[2] + 1 - cart[3]) % 4
            cart[3] = (cart[3] + 1) % 3

        for j in range(len(order)):
            if i == j:
                continue
            other = order[j]
            if cart[0] == other[0] and cart[1] == other[1]:
                print('{},{}'.format(cart[1], cart[0]))
                sys.exit(0)
