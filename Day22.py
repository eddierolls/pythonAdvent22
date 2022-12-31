# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:03:05 2022

@author: edwar
"""
dirs = ["U","R","D","L"]
digs = "0123456789"

class Square(object):
    def __init__(self,coord,isWall):
        self.coord = coord
        self.isWall = isWall
        self.adjacent = {d:None for d in dirs}
    
    def __str__(self):
        if self.isWall:
            return '#'
        else:
            return '.'

def printGrid(grid):
    for line in grid:
        for ix in range(len(line)):
            if line[ix] is None:
                line[ix]=' '
            else:
                line[ix]=str(line[ix])
        print(''.join(line))

# Initialize
grid = []
f = open("inputs/Day22.txt")
xDim = 0
for line in f:
    if line=='\n':
        break
    grid.append(list(line.strip('\n')))
    xDim = max(len(grid[-1]),xDim)
yDim = len(grid)
instructions = f.readline().strip()

# Fill empty grid and populate with Squares
for iy in range(yDim):
    grid[iy]+=[' ']*(xDim-len(grid[iy]))
    for ix in range(len(grid[iy])):
        if grid[iy][ix]=='#':
            grid[iy][ix] = Square((iy,ix),True)
        elif grid[iy][ix]=='.':
            grid[iy][ix] = Square((iy,ix),False)
        elif grid[iy][ix]==' ':
            grid[iy][ix] = None

# Define the adjacent to each square in each row
for iy in range(yDim):
    # Moving left to right
    lineStart = None
    for ix in range(xDim):
        if grid[iy][ix] is not None and lineStart is None:
            lineStart = ix
            grid[iy][ix].adjacent["R"] = (iy,ix+1)
        elif grid[iy][ix] is not None and ix+1==xDim:
            grid[iy][ix].adjacent["R"] = (iy,lineStart)
            lineEnd = ix
        elif grid[iy][ix] is not None and grid[iy][ix+1] is None:
            grid[iy][ix].adjacent["R"] = (iy,lineStart)
            lineEnd = ix
        elif grid[iy][ix] is not None:
            grid[iy][ix].adjacent["R"] = (iy,ix+1)
    # Moving right to left
    for ix in range(xDim):
        if grid[iy][ix] is not None and ix==0:
            grid[iy][ix].adjacent["L"] = (iy,lineEnd)
        elif grid[iy][ix] is not None and grid[iy][ix-1] is None:
            grid[iy][ix].adjacent["L"] = (iy,lineEnd)
            lineEnd = ix
        elif grid[iy][ix] is not None:
            grid[iy][ix].adjacent["L"] = (iy,ix-1)
# In each column
for ix in range(xDim):
    # Moving up to down
    lineStart = None
    for iy in range(yDim):
        if grid[iy][ix] is not None and lineStart is None:
            lineStart = iy
            grid[iy][ix].adjacent["D"] = (iy+1,ix)
        elif grid[iy][ix] is not None and iy+1==yDim:
            grid[iy][ix].adjacent["D"] = (lineStart,ix)
            lineEnd = iy
        elif grid[iy][ix] is not None and grid[iy+1][ix] is None:
            grid[iy][ix].adjacent["D"] = (lineStart,ix)
            lineEnd = iy
        elif grid[iy][ix] is not None:
            grid[iy][ix].adjacent["D"] = (iy+1,ix)
    # Moving down to up
    for iy in range(yDim):
        if grid[iy][ix] is not None and iy==0:
            grid[iy][ix].adjacent["U"] = (lineEnd,ix)
        elif grid[iy][ix] is not None and grid[iy-1][ix] is None:
            grid[iy][ix].adjacent["U"] = (lineEnd,ix)
        elif grid[iy][ix] is not None:
            grid[iy][ix].adjacent["U"] = (iy-1,ix)

# Point to adjacent squares
for iy in range(yDim):
    for ix in range(xDim):
        if grid[iy][ix] is not None:
            for d in dirs:
                adj = grid[iy][ix].adjacent[d]
                if grid[adj[0]][adj[1]].isWall:
                    grid[iy][ix].adjacent[d] = grid[iy][ix]
                else:
                    grid[iy][ix].adjacent[d] = grid[adj[0]][adj[1]]

# Now get onto the instructions!
sq = grid[0][min([ix for ix in range(xDim) if grid[0][ix] is not None])]
heading = 1
ix = 0
while ix<len(instructions):
    ixEnd = ix
    while ixEnd+1<len(instructions) and instructions[ixEnd+1] in digs:
        ixEnd+=1
    moves = int(instructions[ix:ixEnd+1])
    ix = ixEnd+1
    if ix<len(instructions):
        for _ in range(moves):
            sq = sq.adjacent[dirs[heading]]
        if instructions[ix]=='L':
            heading = (heading-1)%4
        elif instructions[ix]=='R':
            heading = (heading+1)%4
        ix+=1

        
print((sq.coord[0]+1)*1000+(sq.coord[1]+1)*4+(heading-1)%4)

