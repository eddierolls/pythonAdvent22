# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 19:55:08 2022

@author: edwar
"""

ints = ''.join(list(map(str,list(range(10)))))

def intify(arr):
    ix=0
    while ix<len(arr):
        iy=0
        while arr[ix+iy] in ints:
            iy+=1
        if iy>0:
            arr = arr[:ix] + [int(''.join(arr[ix:ix+iy]))] + arr[ix+iy:]
        ix+=1
    return arr

def linesLessThan(line1,line2):    
    winner = None
    ix = 0
    while not winner and ix<len(line1) and ix<len(line2):
        if line1[ix]==line2[ix]:
            ix+=1
        elif line1[ix]=='[' and type(line2[ix])==int:
            line2 = line2[:ix]+['[']+[line2[ix]]+[']']+line2[ix+1:]
        elif line2[ix]=='[' and type(line1[ix])==int:
            line1 = line1[:ix]+['[']+[line1[ix]]+[']']+line1[ix+1:]
        elif line1[ix]==']' and line2[ix]!=']':
            winner = 'left'
        elif line1[ix]!=']' and line2[ix]==']':
            winner = 'right'
        elif type(line1[ix])==int and type(line2[ix])==int:
            if line1[ix]<line2[ix]:
                winner = 'left'
            else:
                winner = 'right'
        else:            
            raise ValueError("Expected a line type")
    return winner=='left'

def mergeIn(allLines,line):
    rLim = len(allLines)
    lLim = 0
    ix = (rLim+lLim)//2
    while lLim!=rLim:
        if linesLessThan(line,allLines[ix]):
            rLim = ix
        else:
            lLim = ix+1
        ix = (rLim+lLim)//2
    allLines.insert(ix,line)

f = open("inputs/Day13.txt")
score = 0
pairCount = 1
allLines = [intify(list(x)) for x in ["[[2]]","[[6]]"]]
for line1 in f:
    line1 = list(line1.strip())
    line2 = list(f.readline().strip())
    line1 = intify(line1)
    line2 = intify(line2)
    # Part A
    if linesLessThan(line1,line2):
        score+=pairCount

    # Part B - Realized late on a proper sorting algo is overkill as we just care about the number less than [[2]] and less than [[6]]
    mergeIn(allLines,line1)
    mergeIn(allLines,line2)
    f.readline()
    pairCount+=1
print(score)
for ix in range(len(allLines)):
    if allLines[ix]==intify(list("[[2]]")):
        start=ix+1
    if allLines[ix]==intify(list("[[6]]")):
        end=ix+1
        print(start*end)