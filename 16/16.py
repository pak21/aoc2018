#!/usr/bin/python3

import re
import sys

def addr(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]] + registers[opcodes[2]]
def addi(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]] + opcodes[2]
def mulr(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]] * registers[opcodes[2]]
def muli(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]] * opcodes[2]
def banr(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]] & registers[opcodes[2]]
def bani(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]] & opcodes[2]
def borr(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]] | registers[opcodes[2]]
def bori(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]] | opcodes[2]
def setr(opcodes, registers): registers[opcodes[3]] = registers[opcodes[1]]
def seti(opcodes, registers): registers[opcodes[3]] = opcodes[1]
def gtir(opcodes, registers): registers[opcodes[3]] = 1 if opcodes[1] > registers[opcodes[2]] else 0
def gtri(opcodes, registers): registers[opcodes[3]] = 1 if registers[opcodes[1]] > opcodes[2] else 0
def gtrr(opcodes, registers): registers[opcodes[3]] = 1 if registers[opcodes[1]] > registers[opcodes[2]] else 0
def eqir(opcodes, registers): registers[opcodes[3]] = 1 if opcodes[1] == registers[opcodes[2]] else 0
def eqri(opcodes, registers): registers[opcodes[3]] = 1 if registers[opcodes[1]] == opcodes[2] else 0
def eqrr(opcodes, registers): registers[opcodes[3]] = 1 if registers[opcodes[1]] == registers[opcodes[2]] else 0

pattern = re.compile(r'.*: *\[(\d), (\d), (\d), (\d)\]')

state = 0
testcases = []
with open(sys.argv[1]) as f:
    for line in f:
        if state == 0:
            testcase = [[int(i) for i in pattern.match(line).groups()]]
        elif state == 1:
            testcase.append([int(i) for i in line.split()])
        elif state == 2:
            testcase.append([int(i) for i in pattern.match(line).groups()])
            testcases.append(testcase)
        state = (state + 1) % 4

instructions = [
        addr, addi,
        mulr, muli,
        banr, bani,
        borr, bori,
        setr, seti,
        gtir, gtri, gtrr,
        eqir, eqri, eqrr
        ]

possibles = [set(instructions) for i in range(16)]

threeormore = 0
for testcase in testcases:
    matches = 0
    for fn in instructions:
        registers = [r for r in testcase[0]]
        fn(testcase[1], registers)
        if registers == testcase[2]: # Part 1
            matches += 1
        else: # Part 2
            possibles[testcase[1][0]].discard(fn)
    if matches >= 3:
        threeormore += 1

print('Part 1: {}'.format(threeormore))

definites = [None] * 16
definite_count = 0

while definite_count < 16:
    index, opcode = [(i, list(p)[0]) for i, p in enumerate(possibles) if len(p) == 1][0]
    definites[index] = opcode
    for p in possibles:
        p.discard(opcode)
    definite_count += 1

registers = [0, 0, 0, 0]
with open(sys.argv[2]) as f:
    for line in f:
        opcodes = [int(i) for i in line.split()]
        definites[opcodes[0]](opcodes, registers)

print('Part 2: {}'.format(registers[0]))
