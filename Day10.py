# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:27:35 2022

@author: edwar
"""
def manageCycle(cycleNo,cycleCheck,xReg,score,picture):
    cycleNo+=1
    if cycleNo in cycleCheck:
        score+=xReg*cycleNo
    spritePos = (cycleNo-1)%40
    if abs(xReg-spritePos)<=1:
        picture.append('#')
    else:
        picture.append('.')
    return cycleNo,score

# Part A
f = open('inputs/Day10.txt')
cycleNo = 0
xReg = 1
score = 0
cycleCheck = [20+40*x for x in range(6)]
picture = []

for line in f:
    cycleNo,score = manageCycle(cycleNo,cycleCheck,xReg,score,picture)
    if line.startswith("addx"):
        cycleNo,score = manageCycle(cycleNo,cycleCheck,xReg,score,picture)
        xReg+=int(line.strip().split(' ')[1])
print(score)
for i in range(6):
    print(''.join(picture[i*40:(i+1)*40]))

