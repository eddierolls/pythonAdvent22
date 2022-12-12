# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:05:44 2022

@author: edwar
"""
import string

def onGrid(pos,gridSize):
    return pos[0]>=0 and pos[1]>=0 and pos[0]<gridSize[0] and pos[1]<gridSize[1]

allMoves = [(0,1),(1,0),(0,-1),(-1,0)]

stringMap = {string.ascii_lowercase[i]:i for i in range(26)}

f = open("inputs/Day12.txt")
grid = []
start = None
end = None
lineNo = 0
for line in f:
    line = line.strip()
    if "S" in line:
        ixS = line.index("S")
        start = (lineNo,ixS)
        line = line[:ixS]+'a'+line[ixS+1:]
    if "E" in line:
        ixE = line.index("E")
        line = line[:ixE]+'z'+line[ixE+1:]
        end = (lineNo,ixE)
    grid.append([stringMap[s] for s in line])
    assert len(grid[-1])==len(grid[0])
    lineNo+=1
gridSize = (len(grid),len(grid[0]))

# Part A
totalMoves = 0
endFound = False
posList = [start]
nextPos = []
visited = set([start])
while not endFound and len(posList)>0:
    totalMoves+=1
    for pos in posList:
        posScore = grid[pos[0]][pos[1]]
        for thisMove in allMoves:
            nextSq = (pos[0]+thisMove[0],pos[1]+thisMove[1])
            if onGrid(nextSq,gridSize):
                nextScore = grid[nextSq[0]][nextSq[1]]
                if posScore-nextScore>=-1 and nextSq==end:
                    endFound=True
                    break
                elif posScore-nextScore>=-1 and nextSq not in visited:
                    visited.add(nextSq)
                    nextPos.append(nextSq)
    posList = nextPos
    nextPos = []

print(totalMoves)

# Part B
totalMoves = 0
endFound = False
posList = [end]
nextPos = []
visited = set([end])
while not endFound and len(posList)>0:
    totalMoves+=1
    for pos in posList:
        posScore = grid[pos[0]][pos[1]]
        for thisMove in allMoves:
            nextSq = (pos[0]+thisMove[0],pos[1]+thisMove[1])
            if onGrid(nextSq,gridSize):
                nextScore = grid[nextSq[0]][nextSq[1]]
                if posScore-nextScore<=1 and nextScore==0:
                    endFound=True
                    break
                elif posScore-nextScore<=1 and nextSq not in visited:
                    visited.add(nextSq)
                    nextPos.append(nextSq)
    posList = nextPos
    nextPos = []

print(totalMoves)