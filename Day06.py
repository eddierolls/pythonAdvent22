# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:40:23 2022

@author: edwar
"""

from collections import deque

f = open('inputs/Day06.txt')
printA = True
for line in f:
    buffer = deque([' ']*14)
    score = 0
    partA = False
    for s in line:
        buffer.popleft()
        buffer.append(s)
        score+=1
        if len(set(list(buffer)[-4:]))==4 and score>=4 and not partA:
            partA = True
            if printA:
                print(score)
        elif len(set(buffer))==14 and score>=14:
            print(score)
            break