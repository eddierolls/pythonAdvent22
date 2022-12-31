# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:07:03 2022

@author: edwar
"""
from collections import defaultdict

dirCheck = {0:[(0,-1),(1,-1),(-1,-1)],
            1:[(0,1),(1,1),(-1,1)],
            2:[(-1,0),(-1,1),(-1,-1)],
            3:[(1,0),(1,1),(1,-1)]}
allDirs = [(i,j) for i in range(-1,2) for j in range(-1,2) if (i!=0 or j!=0)]
ROUNDS = 10

class Elf(object):
    def __init__(self,pos):
        self.pos = pos
        self.proposal = None

f = open("inputs/Day23.txt")
elves = []
iy = 0
for line in f:
    line = line.strip()
    for ix in range(len(line)):
        if line[ix]=='#':
            elves.append(Elf((ix,iy)))
    iy+=1

# Loop over rounds
elvesThis = [1] # Placeholder
r=0
while len(elvesThis)>0:
    # Step 1: find elf positions
    allPos = set([elf.pos for elf in elves])
    # Step 2: find all elves who might move this turn
    elvesThis = []
    for elf in elves:
        adj = False
        for d in allDirs:
            if (elf.pos[0]+d[0],elf.pos[1]+d[1]) in allPos:
                adj = True
                break
        if adj:
            elvesThis.append(elf)
    # Step 3: Get all prposals
    proposals = defaultdict(int)
    for elf in elvesThis:
        for ixD in range(r,r+4):
            ixD%=4
            adj = False
            for sq in dirCheck[ixD]:
                if (elf.pos[0]+sq[0],elf.pos[1]+sq[1]) in allPos:
                    adj = True
            if not adj:
                prop = (elf.pos[0]+dirCheck[ixD][0][0],elf.pos[1]+dirCheck[ixD][0][1])
                proposals[prop] += 1
                elf.proposal = prop
                break
    # Step 4: Move to proposals
    for elf in elvesThis:
        if elf.proposal is not None and proposals[elf.proposal]==1:
            elf.pos = elf.proposal
        # Step 5: Clear proposals
        elf.proposal = None
    r+=1
    if r==10:
        minRect = [min([elf.pos[0] for elf in elves]),
                   max([elf.pos[0] for elf in elves]),
                   min([elf.pos[1] for elf in elves]),
                   max([elf.pos[1] for elf in elves])]
        print((minRect[1]-minRect[0]+1)*(minRect[3]-minRect[2]+1)-len(elves))

print(r)