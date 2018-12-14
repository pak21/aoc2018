#!/usr/bin/python3

import sys

class Marble:
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

with open(sys.argv[1]) as f:
    for line in f:
        players, marbles = [int(x) for x in line.split()]

        marble = Marble(0)
        scores = [0] * players
        for i in range(1, marbles + 1):
            if i % 23 == 0:
                toremove = marble.prev.prev.prev.prev.prev.prev.prev
                scores[i % players] += i + toremove.value
                toremove.remove()
                marble = toremove.next
            else:
                newmarble = Marble(i)
                marble.next.insertafter(newmarble)
                marble = newmarble
        print(max(scores))
