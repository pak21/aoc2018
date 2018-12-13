#!/usr/bin/python3

from operator import itemgetter
import re
import sys

pattern = re.compile('position=< *([-\d]+), *([-\d]+)> velocity=< *([-\d]+), *([-\d]+)>')

with open(sys.argv[1]) as f:
    particles = [[int(x) for x in pattern.match(line).groups()] for line in f]

lastr = 9999999
time = -1
while True:
    minx = min(particles, key=itemgetter(0))[0]
    maxx = max(particles, key=itemgetter(0))[0]
    r = maxx - minx
    if r > lastr:
        break

    for p in particles:
        p[0] += p[2]
        p[1] += p[3]
    time += 1
    lastr = r

for p in particles:
    p[0] -= p[2]
    p[1] -= p[3]

minx = min(particles, key=itemgetter(0))[0]
maxx = max(particles, key=itemgetter(0))[0]
miny = min(particles, key=itemgetter(1))[1]
maxy = max(particles, key=itemgetter(1))[1]

rx = maxx - minx + 1
ry = maxy - miny + 1

picture = [ ['.'] * rx for i in range(ry) ]
for p in particles:
    picture[p[1] - miny][p[0] - minx] = 'X'
for row in picture:
    print(''.join(row))

print(time)
