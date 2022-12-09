# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:51:27 2022

@author: edwar
"""

f = open("inputs/Day09.txt")
dirDict = {'R':(1,0),'U':(0,1),'L':(-1,0),'D':(0,-1)}
allPos = set()
head = [0,0]
tail = [0,0]
for line in f:
    newDir,steps = line.strip().split(' ')
    newDir = dirDict[newDir]
    for _ in range(int(steps)):
        mainId = int(newDir[1]!=0)
        otherId = 1-mainId
        head[mainId] += newDir[mainId]
        if abs(head[mainId]-tail[mainId])==2 and head[otherId]==tail[otherId]:
            tail[mainId]+=(head[mainId]-tail[mainId])//2
        elif abs(head[mainId]-tail[mainId])==2:
            tail[mainId]+=(head[mainId]-tail[mainId])//2
            tail[otherId] = head[otherId]
        allPos.add(tuple(tail))

print(len(allPos))
            