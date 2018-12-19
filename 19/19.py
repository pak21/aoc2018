#!/usr/bin/python3

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

instructions = {
        'addr': addr,
        'addi': addi,
        'mulr': mulr,
        'muli': muli,
        'banr': banr,
        'bani': bani,
        'borr': borr,
        'bori': bori,
        'setr': setr,
        'seti': seti,
        'gtir': gtir,
        'gtri': gtri,
        'gtrr': gtrr,
        'eqir': eqir,
        'eqri': eqri,
        'eqrr': eqrr
}

opcodes = []
with open(sys.argv[1]) as f:
    ipreg = int(f.readline().split()[1])
    for line in f:
        x = line.split()
        opcodes.append((x[0], int(x[1]), int(x[2]), int(x[3])))

registers = [1, 0, 0, 0, 0, 0]

while registers[ipreg] < len(opcodes):
    instruction = opcodes[registers[ipreg]]
    if registers[ipreg] == 3:
        if registers[5] % 1000000 == 0:
            print('{}/{}'.format(registers[5], registers[1]))
        if registers[1] % registers[5] == 0:
            registers[0] += registers[5]
        registers[ipreg] = 12
    else:
        fn = instructions[instruction[0]]
        fn(instruction, registers)
        registers[ipreg] += 1

print(registers[0])
