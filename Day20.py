# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 19:57:04 2022

@author: edwar
"""

PART1 = False
if PART1:
    REPEATS = 1
    MULT = 1
else:
    REPEATS = 10
    MULT = 811589153

f = open('inputs/Day20.txt')
seqMap = {}
ixF = 0
for line in f:
    seqMap[ixF] = int(line.strip())*MULT
    ixF+=1

N = len(seqMap)
pos = list(range(N))
for _ in range(REPEATS):
    for ixP in range(N):
        ix = pos.index(ixP)
        pos.pop(ix)
        ixNew = (ix+seqMap[ixP])%(N-1)
        if ixNew==0 and seqMap[ixP]<0:
            ixNew = N
        pos.insert(ixNew,ixP)
    
out = [seqMap[pos[x]] for x in range(N)]
ixStart = out.index(0)
print(sum([out[(ixStart+ix)%N] for ix in [1000,2000,3000]]))
