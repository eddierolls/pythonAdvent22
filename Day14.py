# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:57:43 2022

@author: edwar
"""

f = open("inputs/Day14.txt")
lineList = []
xLim = [500,500]
yLim = [0,0]
for line in f:
    line = line.strip()
    line = line.split(' -> ')
    barrierList = []
    for l in line:
        l = tuple(map(int,l.split(',')))
        xLim = [min(xLim[0],l[0]),max(xLim[1],l[0])]
        yLim = [min(yLim[0],l[1]),max(yLim[1],l[1])]
        barrierList.append(l)
    lineList.append(barrierList)

grid = [[False for _ in range(yLim[1]+2)] + [True] for _ in range(xLim[1]+yLim[1]+1)]


for line in lineList:
    for ix in range(len(line)-1):
        start = line[ix]
        end = line[ix+1]
        if start>end:
            end,start = start,end
        if start[0]<end[0]:
            for x in range(start[0],end[0]+1):
                grid[x][start[1]] = True
        elif start[1]<end[1]:
            for y in range(start[1],end[1]+1):
                grid[start[0]][y] = True
        else:
            raise ValueError("Sort didn't work!")
        
s = 0
finished = False
partA = None
while not finished:
    pos = [500,0]
    falling = True
    while falling:
        if not partA and pos[1]>yLim[1]:
            partA = s
        if not grid[pos[0]][pos[1]+1]:
            pos = [pos[0],pos[1]+1]
        elif not grid[pos[0]-1][pos[1]+1]:
            pos = [pos[0]-1,pos[1]+1]
        elif not grid[pos[0]+1][pos[1]+1]:
            pos = [pos[0]+1,pos[1]+1]
        else:
            grid[pos[0]][pos[1]] = True
            falling = False
    if pos==[500,0]:
        finished = True
    s+=1

print(partA)
print(s)

