#!/usr/bin/python3

import collections
import sys

class Recipe:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = self

    def insertafter(self, after):
        after.prev = self
        after.next = self.next
        after.next.prev = after
        self.next = after

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

def dump(head):
    current = head
    values = []
    while True:
        values.append(current.value)
        current = current.next
        if current == head:
            break
    print(values)

r1 = Recipe(3)
r2 = Recipe(7)
r1.insertafter(r2)
head = r1
tail = r2

numadded = 2
trigger = '190221'[::-1]
foo = ''
seen = collections.defaultdict(int)
while True:
    toadd = r1.value + r2.value
    for c in str(toadd):
        numadded += 1
        foo = c + foo
        foo = foo[:len(trigger)]
        seen[foo] += 1
        if foo == trigger:
            print(numadded - len(trigger))
            sys.exit(0)
        if numadded % 100000 == 0:
            print(numadded, len(seen))
        newrecipe = Recipe(int(c))
        tail.insertafter(newrecipe)
        tail = newrecipe

    for i in range(1 + r1.value):
        r1 = r1.next
    for i in range(1 + r2.value):
        r2 = r2.next
