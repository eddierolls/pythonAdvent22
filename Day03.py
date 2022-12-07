# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:39:43 2022

@author: edwar
"""
import string

def readThreeLines(f):
    bp1 = f.readline().strip()
    if bp1=='':
        return (None,None,None)
    out = [bp1,f.readline().strip(),f.readline().strip()]
    out = [set(x) for x in out]
    return out

scoreDict = {string.ascii_letters[x]:x+1 for x in range(52)}
f = open('inputs/Day03.txt')
score=0
for line in f:
    line = line.strip()
    n = len(line)
    a,b = (set(line[:n//2]),set(line[n//2:]))
    shared = a.intersection(b)
    assert len(shared)==1
    score += scoreDict[list(shared)[0]]

print(score)

# Part 2

f = open('inputs/Day03.txt')
score=0

(bp1,bp2,bp3) = readThreeLines(f)
while bp1 is not None:
    shared = bp1.intersection(bp2).intersection(bp3)
    assert len(shared)==1
    score += scoreDict[list(shared)[0]]
    (bp1,bp2,bp3) = readThreeLines(f)

print(score)