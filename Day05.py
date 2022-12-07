# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:51:06 2022

@author: edwar
"""
from copy import deepcopy
from time import sleep

filename = "inputs/Day05.txt"

f = open(filename)
queueSize = 0
queueLine = 0
for line in f:
    if line[1]=='1':
        queueSize = max(map(int,line.split()))
        break
    queueLine+=1

f.close()

f = open(filename)
pilesA = [[] for _ in range(queueSize)]
for _ in range(queueLine):
    line = f.readline()
    for pileNo in range(queueSize):
        s = line[pileNo*4+1]
        if s!=' ':
            pilesA[pileNo].append(s)
    
pilesA = [list(reversed(p)) for p in pilesA]
pilesB = deepcopy(pilesA)

f.readline()
f.readline()

for line in f:
    cmd = line.strip().split(' ')
    moveCt = int(cmd[1])
    pileFrom = int(cmd[3])-1
    pileTo = int(cmd[5])-1
    # Part 1
    for _ in range(moveCt):
        s = pilesA[pileFrom][-1]
        pilesA[pileFrom] = pilesA[pileFrom][:-1]
        pilesA[pileTo].append(s)
    # Part 2
    s = pilesB[pileFrom][-moveCt:]
    pilesB[pileFrom] = pilesB[pileFrom][:-moveCt]
    pilesB[pileTo] = pilesB[pileTo] + s
    
print(''.join([p[-1] for p in pilesA]))
print(''.join([p[-1] for p in pilesB]))
        
    
