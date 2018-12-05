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
        minafter = len(original)
        for r in range(26):
            lowercase = chr(r + 97)
            uppercase = chr(r + 65)
            polymer = original.replace(lowercase, '').replace(uppercase, '')
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
            if len(polymer) < minafter:
                minafter = len(polymer)
        print(minafter)
