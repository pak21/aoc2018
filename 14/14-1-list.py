#!/usr/bin/python3

import sys

recipes = [3, 7]
r1 = 0
r2 = 1
trigger = 190221
while True:
    toadd = recipes[r1] + recipes[r2]
    for c in str(toadd):
        recipes.append(int(c))
        if len(recipes) == trigger + 10:
            print(''.join([str(i) for i in recipes[-10:]]))
            sys.exit(0)

    r1 = (r1 + 1 + recipes[r1]) % len(recipes)
    r2 = (r2 + 1 + recipes[r2]) % len(recipes)
