# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:46:45 2022

@author: edwar
"""

f = open('inputs/Day01.txt')
allElves = []
currentElf = 0
for line in f:
    if line=='\n':
        allElves.append(currentElf)
        currentElf = 0
    else:
        currentElf += int(line)

allElves.append(currentElf)
allElves.sort(reverse=True)
print(allElves[0])
print(sum(allElves[0:3]))

