#!/usr/bin/python3

import collections
import datetime
import operator
import re
import sys

with open(sys.argv[1]) as f:
    for polymer in f:
        polymer = polymer.rstrip()
        original = polymer
        found = True
        while found:
            found = False
            for l in range(26):
                a = chr(l + 65) + chr(l + 97)
                b = a[::-1]
                if a in polymer:
                    polymer = polymer.replace(a, '')
                    found = True
                if b in polymer:
                    polymer = polymer.replace(b, '')
                    found = True
        print('{} -> {}'.format(original, polymer))
        print('{} -> {}'.format(len(original), len(polymer)))
