# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:47:36 2022

@author: edwar
"""
from collections import Counter

def updateCounter(c,t):
    for i in range(t+1):
        c[i]=1
    for i in range(t+1,10):
        c[i]+=1

f = open("inputs/Day08.txt")
rows = []
tallestTrees = []
for line in f:
    rows.append(list(map(int,[s for s in line.strip()])))
    tallestTrees.append([False]*len(rows[-1]))

# Part A
for ixR in range(len(rows)):
    row = rows[ixR]
    currentMax = -1
    for ixC in range(len(row)):
        c = row[ixC]
        if c>currentMax:
            currentMax=c
            tallestTrees[ixR][ixC] = True
    currentMax = -1
    for ixC in range(len(row)-1,-1,-1):
        c = row[ixC]
        if c>currentMax:
            currentMax=c
            tallestTrees[ixR][ixC] = True
            
for ixC in range(len(rows[0])):
    currentMax = -1
    for ixR in range(len(rows)):
        if rows[ixR][ixC]>currentMax:
            currentMax = rows[ixR][ixC]
            tallestTrees[ixR][ixC] = True
    currentMax = -1
    for ixR in range(len(rows)-1,-1,-1):
        if rows[ixR][ixC]>currentMax:
            currentMax = rows[ixR][ixC]
            tallestTrees[ixR][ixC] = True

score = 0
for ixR in range(len(rows)):
    for ixC in range(len(rows[ixR])):
        score+=tallestTrees[ixR][ixC]
print(score)

# Part B
treeScores = []
for ixR in range(len(rows)):
    treeScores.append([])
    c = Counter() # If i look back along the row, how many spaces until I see a tree taller than this
    for ixC in range(len(rows[0])):
        t = rows[ixR][ixC]
        treeScores[-1].append((c[t]))
        updateCounter(c,t)
    c = Counter() # If i look back along the row, how many spaces until I see a tree taller than this
    for ixC in range(len(rows[0])-1,-1,-1):
        t = rows[ixR][ixC]
        treeScores[ixR][ixC]*=c[t]
        updateCounter(c,t)

for ixC in range(len(rows[0])):
    c = Counter()
    for ixR in range(len(rows)):
        t = rows[ixR][ixC]
        treeScores[ixR][ixC]*=c[t]
        updateCounter(c,t)
    c = Counter()
    for ixR in range(len(rows)-1,-1,-1):
        t = rows[ixR][ixC]
        treeScores[ixR][ixC]*=c[t]
        updateCounter(c,t)

score = 0
for ixR in range(len(rows)):
    for ixC in range(len(rows[ixR])):
        score=max(treeScores[ixR][ixC],score)
print(score)
