# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:35:39 2022

@author: edwar
"""
def fullyContains(a,b):
    return a[0]<=b[0] and a[1]>=b[1]

def anyOverlap(a,b):
    return (a[0]<=b[0] and b[0]<=a[1]) or (b[0]<=a[0] and a[0]<=b[1])

f = open('inputs/Day04.txt')

score = 0
score2 = 0
for line in f:
    a,b = line.strip().split(',')
    a = list(map(int,a.split('-')))
    b = list(map(int,b.split('-')))
    if fullyContains(a,b) or fullyContains(b,a):
        score+=1
    if anyOverlap(a,b):
        score2+=1

print(score)
print(score2)
