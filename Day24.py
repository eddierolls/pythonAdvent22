# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 08:52:25 2022

@author: edwar
"""
dirMap = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
allMoves = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

class Blizzard(object):
    def __init__(self,direction,pos):
        self.direction = direction
        self.move = dirMap[direction]
        self.pos = pos

def isValidPosition(dims,sq,start=None):
    if sq==start or (sq[0]>=1 and sq[0]<=dims[0]-2 and sq[1]>=1 and sq[1]<=dims[1]-2):
        return True
    else:
        return False
    
def moveBlizzards(blizzards):
    for b in blizzards:
        nextPos = (b.pos[0]+b.move[0],b.pos[1]+b.move[1])
        if isValidPosition(dims,nextPos):
            b.pos = nextPos
        else:
            if b.direction=='^':
                b.pos = (dims[0]-2,b.pos[1])
            elif b.direction=='>':
                b.pos = (b.pos[0],1)
            elif b.direction=='v':
                b.pos = (1,b.pos[1])
            elif b.direction=='<':
                b.pos = (b.pos[0],dims[1]-2)

def updateStates(states,allBlizzards,start,end,dims):
    complete = False
    nextStates = set()
    for state in states:
        for move in allMoves:
            proposed = (state[0]+move[0],state[1]+move[1])
            if proposed==end:
                complete = True
            elif proposed not in allBlizzards and isValidPosition(dims,proposed,start):
                nextStates.add(proposed)
    return complete,nextStates

def runSimulation(blizzards,start,end):
    complete = False
    moves = 0
    states = set([start])
    while not complete and len(states)>0:
        # Step 1: move all blizzards
        moveBlizzards(blizzards)
        # Step 2: get a list of all blizzard position
        allBlizzards = set([b.pos for b in blizzards])    
        # Step 3: loop over all current positions and move to them
        complete,states = updateStates(states,allBlizzards,start,end,dims)
        moves+=1
    return moves

f = open('inputs/Day24.txt')
blizzards = []
iy = 0
for line in f:
    line = line.strip()
    for ix in range(len(line)):
        if line[ix] in dirMap.keys():
            blizzards.append(Blizzard(line[ix],(iy,ix)))
    iy+=1
    dims = [iy,len(line)]


start = (0,1)
end = (dims[0]-1,dims[1]-2)
moves = []
moves.append(runSimulation(blizzards,start,end))
moves.append(runSimulation(blizzards,end,start))
moves.append(runSimulation(blizzards,start,end))
print(sum(moves))

    
    
    