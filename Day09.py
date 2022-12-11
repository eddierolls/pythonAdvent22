# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:51:27 2022

@author: edwar
"""
from math import copysign

f = open("inputs/Day09.txt")
dirDict = {'R':(1,0),'U':(0,1),'L':(-1,0),'D':(0,-1)}
allPos = set()
ROPELEN = 10
rope = [[0,0] for _ in range(ROPELEN)]
for line in f:
    newDir,steps = line.strip().split(' ')
    newDir = dirDict[newDir]
    for _ in range(int(steps)):
        rope[0] = [rope[0][i]+newDir[i] for i in range(2)]
        for ropePos in range(1,ROPELEN):
            for mainId in range(2):
                otherId = 1-mainId
                if abs(rope[ropePos-1][mainId]-rope[ropePos][mainId])==2 and rope[ropePos-1][otherId]==rope[ropePos][otherId]:
                    rope[ropePos][mainId]+=(rope[ropePos-1][mainId]-rope[ropePos][mainId])//2
                elif abs(rope[ropePos-1][mainId]-rope[ropePos][mainId])==2:
                    rope[ropePos][mainId]+=(rope[ropePos-1][mainId]-rope[ropePos][mainId])//2
                    rope[ropePos][otherId]+=int(copysign(1,rope[ropePos-1][otherId]-rope[ropePos][otherId]))
        allPos.add(tuple(rope[-1]))
        

print(len(allPos))
            