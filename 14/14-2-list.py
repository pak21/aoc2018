#!/usr/bin/python3

import sys

recipes = [3, 7]
r1 = 0
r2 = 1
trigger = [1, 9, 0, 2, 2, 1]
while True:
    toadd = recipes[r1] + recipes[r2]
    for c in str(toadd):
        recipes.append(int(c))
        if recipes[-len(trigger):] == trigger:
            print(len(recipes) - len(trigger))
            sys.exit(0)

    r1 = (r1 + 1 + recipes[r1]) % len(recipes)
    r2 = (r2 + 1 + recipes[r2]) % len(recipes)
