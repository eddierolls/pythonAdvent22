# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 08:53:30 2022

@author: edwar
"""
CAVEWIDTH = 7
ROCKS = 2022

class Cave(object):
    def __init__(self):
        self.topRock = 0
        self.grid = [[False]*CAVEWIDTH for _ in range(3)]
        self.blocked = set()
    
    def addRock(self,rock):
        self.rock = [(y+self.topRock+3,x) for y,x in rock.coords]

    def moveJet(self,jet):
        moveDict = {'<':-1,'>':1}
        moveDir = moveDict[jet]
        canMove = True
        for y,x in self.rock:
            if (y,x+moveDir) in self.blocked or x+moveDir==CAVEWIDTH or x+moveDir==-1:
                canMove = False
                break
        if canMove:
            self.rock = [(y,x+moveDir) for y,x in self.rock]
    
    def moveDown(self):
        canMove = True
        for y,x in self.rock:
            if (y-1,x) in self.blocked or y-1<0:
                canMove = False
                break
        if canMove:
            self.rock = [(y-1,x) for y,x in self.rock]
        else:
            self.topRock = max(self.topRock,max([r[0]+1 for r in self.rock]))
            self.grid = self.grid + [[False]*CAVEWIDTH for _ in range(self.topRock-len(self.grid)+6)]
            for y,x in self.rock:
                self.blocked.add((y,x))
                self.grid[y][x] = True
        return canMove
    
    def printCave(self):
        drawMap = {False:'.',True:'#'}
        for y in range(len(self.grid)-1,-1,-1):
            print(''.join([drawMap[x] for x in self.grid[y]]))

class Rock(object):
    def __init__(self,shape):
        self.height = len(shape)
        self.coords = []
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                if shape[y][x]=='#':
                    self.coords.append([y,x+2])

# Note the third rock is flipped
inputRocks = [['####'],['.#.','###','.#.'],['###','..#','..#'],['#','#','#','#'],['##','##']]
f = open('inputs/Day17.txt')
pattern = f.readline().strip()

# Part 1
cave = Cave()
ixP = 0
for r in range(ROCKS):
    thisRock = Rock(inputRocks[r%len(inputRocks)])
    cave.addRock(thisRock)
    canMove = True
    while canMove:
        cave.moveJet(pattern[ixP%len(pattern)])
        canMove = cave.moveDown()
        ixP+=1
print(cave.topRock)


