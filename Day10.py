# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:27:35 2022

@author: edwar
"""
f = open('inputs/Day10.txt')
cycleNo = 0
xReg = 1
score = 0
cycleCheck = [20+40*x for x in range(6)]

for line in f:
    cycleNo+=1
    if cycleNo in cycleCheck:
        score+=xReg*cycleNo
    if line.startswith("addx"):
        cycleNo+=1
        if cycleNo in cycleCheck:
            score+=xReg*cycleNo
        xReg+=int(line.strip().split(' ')[1])
print(score)