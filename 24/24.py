#!/usr/bin/python3

import re
import sys

BOOST = 0
BOOST = 46

pattern = re.compile(r'(\d+) units each with (\d+) hit points (?:\((.*)\) )?with an attack that does (\d+) (.+) damage at initiative (\d+)')

class Group():
    def __init__(self, isimmune, units, hp, immune, weak, damage, damagetype, initiative):
        self.isimmune = isimmune
        self.units = units
        self.hp = hp
        self.immune = immune
        self.weak = weak
        self.damage = damage
        self.damagetype = damagetype
        self.initiative = initiative

    def power(self):
        return self.units * self.damage

def potential_damage(attacker, defender):
    damage = attacker.power()
    if attacker.damagetype in defender.weak:
        damage *= 2
    return damage

def select_target(attacker, selected):
    valid_targets = [g for g in groups if g not in selected.values() and g.isimmune != attacker.isimmune and not attacker.damagetype in g.immune]
    return max(valid_targets, key=lambda x: (potential_damage(attacker, x), x.power(), x.initiative)) if valid_targets else None

def attack(attacker, defender):
    defender.units -= min(potential_damage(attacker, defender) // defender.hp, defender.units)

def doround():
    selected = {}
    for group in sorted(groups, key=lambda x: (x.power(), x.initiative), reverse=True):
        target = select_target(group, selected)
        if target:
            selected[group] = target

    for group in sorted([g for g in groups if g in selected and g.units > 0], key=lambda x: x.initiative, reverse=True):
        attack(group, selected[group])

groups = []

with open(sys.argv[1]) as f:
    for unstripped in f:
        line = unstripped.rstrip()

        if line == 'Immune System:':
            isimmune = True
        elif line == 'Infection:':
            isimmune = False
        elif line == '':
            continue
        else:
            immune = set()
            weak = set()
            match = pattern.match(line)
            units, hp, attributes, damage, damagetype, initiative = match.groups()
            if attributes:
                for attribute in attributes.split('; '):
                    a, _, typesstring = attribute.split(' ', maxsplit=2)
                    types = set(typesstring.split(', '))
                    if a == 'immune':
                        immune = types
                    else:
                        weak = types
            damage = int(damage)
            if isimmune:
                damage += BOOST
            groups.append(Group(isimmune, int(units), int(hp), immune, weak, damage, damagetype, int(initiative)))

while True:
    doround()
    groups = [g for g in groups if g.units > 0]
    immune = len([g for g in groups if g.isimmune])
    if immune == 0 or immune == len(groups):
        break

print('Winner: {} with {} units left'.format(groups[0].isimmune, sum([g.units for g in groups])))
