# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:06:08 2022

@author: edwar
"""

# Part A
oppMap = {'A':1, 'B':2, 'C':3} # Rock, Paper, Scissors
scoreMap = {'X':1, 'Y':2, 'Z':3} # Rock, Paper, Scissors
f = open('inputs/Day02.txt')

score = 0
for line in f:
    opp,you = line.strip().split(' ')
    res = (scoreMap[you]-oppMap[opp])%3
    if res==0:
        score+=3
    elif res==1:
        score+=6
    score+=scoreMap[you]
print(score)

# Part B
resMap = {'X':-1, 'Y':0, 'Z':1}
f = open('inputs/Day02.txt')

score = 0
for line in f:
    opp,res = line.strip().split(' ')
    you = ((oppMap[opp]+resMap[res]-1)%3)+1
    score+=you
    score+=3*(1+resMap[res])
print(score)
