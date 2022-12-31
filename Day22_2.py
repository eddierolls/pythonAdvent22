# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:03:05 2022

@author: edwar
"""

TEST = False
if TEST:
    metaDim = (3,4)
else:
    metaDim = (4,3)

dirs = ["U","R","D","L"]
digs = "0123456789"
revDirs = {"U":"D","D":"U","L":"R","R":"L"}

class Square(object):
    def __init__(self,coord,isWall):
        self.coord = coord
        self.isWall = isWall
        self.adjacent = {d:None for d in dirs}
        self.metaSq = None
    
    def __str__(self):
        if self.isWall:
            return '#'
        else:
            return '.'

class MetaSquare(object):
    def __init__(self,num,adjacent):
        self.num = num
        self.adjacent = adjacent
        self.edgeCoord = {}

def checkMetaSquares(metaSquares):
    allVal = []
    for sq in metaSquares:
        allVal+=[x for x in sq.adjacent.values()]
        for d in dirs:
            adj = metaSquares[sq.adjacent[d][0]]
            newDir = sq.adjacent[d][1]
            assert(adj.adjacent[revDirs[newDir]][0]==sq.num)
    assert(24==len(set(allVal)))

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

# Baiscally hard code these
metaSquares = []
if TEST:
    metaSquares.append(MetaSquare(0,{"D":(3,"D"),"U":(1,"D"),"R":(5,"L"),"L":(2,"D")}))
    metaSquares.append(MetaSquare(1,{"D":(4,"U"),"U":(0,"D"),"R":(2,"R"),"L":(5,"U")}))
    metaSquares.append(MetaSquare(2,{"D":(4,"R"),"U":(0,"R"),"R":(3,"R"),"L":(1,"L")}))
    metaSquares.append(MetaSquare(3,{"D":(4,"D"),"U":(0,"U"),"R":(5,"D"),"L":(2,"L")}))
    metaSquares.append(MetaSquare(4,{"D":(1,"U"),"U":(3,"U"),"R":(5,"R"),"L":(2,"U")}))
    metaSquares.append(MetaSquare(5,{"D":(1,"R"),"U":(3,"L"),"R":(0,"L"),"L":(4,"L")}))
else:
    metaSquares.append(MetaSquare(0,{"D":(2,"D"),"U":(5,"R"),"R":(1,"R"),"L":(3,"R")}))
    metaSquares.append(MetaSquare(1,{"D":(2,"L"),"U":(5,"U"),"R":(4,"L"),"L":(0,"L")}))
    metaSquares.append(MetaSquare(2,{"D":(4,"D"),"U":(0,"U"),"R":(1,"U"),"L":(3,"D")}))
    metaSquares.append(MetaSquare(3,{"D":(5,"D"),"U":(2,"R"),"R":(4,"R"),"L":(0,"R")}))
    metaSquares.append(MetaSquare(4,{"D":(5,"L"),"U":(2,"U"),"R":(1,"L"),"L":(3,"L")}))
    metaSquares.append(MetaSquare(5,{"D":(1,"D"),"U":(3,"U"),"R":(4,"U"),"L":(0,"D")}))
checkMetaSquares(metaSquares)

# Assign a meta square to each sqaure
metaSize = xDim//metaDim[1]
assert metaSize==yDim//metaDim[0]
sqIx = 0
for iyM in range(metaDim[0]):
    for ixM in range(metaDim[1]):
        coords = [(iy,ix) for iy in range(iyM*metaSize,(iyM+1)*metaSize) for ix in range(ixM*metaSize,(ixM+1)*metaSize)]
        if grid[coords[0][0]][coords[0][1]] is not None:
            for iy,ix in coords:
                grid[iy][ix].metaSq = metaSquares[sqIx]
            metaSquares[sqIx].edgeCoord = {"U":iyM*metaSize,"D":(iyM+1)*metaSize-1,"L":ixM*metaSize,"R":(ixM+1)*metaSize-1}
            metaSquares[sqIx].topLeft = (iyM*metaSize,ixM*metaSize)
            sqIx+=1

# Define the adjacent to each square in each row (like part 1 but removing the wraparound)
for iy in range(yDim):
    for ix in range(xDim):
        if grid[iy][ix] is not None:
            thisSq = grid[iy][ix]
            iyM = iy - thisSq.metaSq.topLeft[0]
            ixM = ix - thisSq.metaSq.topLeft[1]
            if ix+1<xDim and grid[iy][ix+1] is not None:
                thisSq.adjacent["R"] = (iy,ix+1,"R")
            else:
                adjMeta = thisSq.metaSq.adjacent["R"]
                newDir = adjMeta[1]
                topLeft = metaSquares[adjMeta[0]].topLeft
                edgeCoord = metaSquares[adjMeta[0]].edgeCoord
                if newDir=="R":
                    thisSq.adjacent["R"] = (topLeft[0]+iyM,edgeCoord["L"],newDir)
                elif newDir=="L":
                    thisSq.adjacent["R"] = (topLeft[0]+metaSize-iyM-1,edgeCoord["R"],newDir)
                elif newDir=="U":
                    thisSq.adjacent["R"] = (edgeCoord["D"],topLeft[1]+iyM,newDir)
                elif newDir=="D":
                    thisSq.adjacent["R"] = (edgeCoord["U"],topLeft[1]+metaSize-iyM-1,newDir)
            if ix>0 and grid[iy][ix-1] is not None:
                thisSq.adjacent["L"] = (iy,ix-1,"L")
            else:
                adjMeta = thisSq.metaSq.adjacent["L"]
                newDir = adjMeta[1]
                topLeft = metaSquares[adjMeta[0]].topLeft
                edgeCoord = metaSquares[adjMeta[0]].edgeCoord
                if newDir=="L":
                    thisSq.adjacent["L"] = (topLeft[0]+iyM,edgeCoord["R"],newDir)
                elif newDir=="R":
                    thisSq.adjacent["L"] = (topLeft[0]+metaSize-iyM-1,edgeCoord["L"],newDir)
                elif newDir=="D":
                    thisSq.adjacent["L"] = (edgeCoord["U"],topLeft[1]+iyM,newDir)
                elif newDir=="U":
                    thisSq.adjacent["L"] = (edgeCoord["D"],topLeft[1]+metaSize-iyM-1,newDir)
# In each column
for ix in range(xDim):
    for iy in range(yDim):
        if grid[iy][ix] is not None:
            thisSq = grid[iy][ix]
            iyM = iy - thisSq.metaSq.topLeft[0]
            ixM = ix - thisSq.metaSq.topLeft[1]
            if iy>0 and grid[iy-1][ix] is not None:
                thisSq.adjacent["U"] = (iy-1,ix,"U")
            else:
                adjMeta = thisSq.metaSq.adjacent["U"]
                newDir = adjMeta[1]
                topLeft = metaSquares[adjMeta[0]].topLeft
                edgeCoord = metaSquares[adjMeta[0]].edgeCoord
                if newDir=="R":
                    thisSq.adjacent["U"] = (topLeft[0]+ixM,edgeCoord["L"],newDir)
                elif newDir=="L":
                    thisSq.adjacent["U"] = (topLeft[0]+metaSize-ixM-1,edgeCoord["R"],newDir)
                elif newDir=="U":
                    thisSq.adjacent["U"] = (edgeCoord["D"],topLeft[1]+ixM,newDir)
                elif newDir=="D":
                    thisSq.adjacent["U"] = (edgeCoord["U"],topLeft[1]+metaSize-ixM-1,newDir)
            if iy+1<yDim and grid[iy+1][ix] is not None:
                thisSq.adjacent["D"] = (iy+1,ix,"D")
            else:
                adjMeta = thisSq.metaSq.adjacent["D"]
                newDir = adjMeta[1]
                topLeft = metaSquares[adjMeta[0]].topLeft
                edgeCoord = metaSquares[adjMeta[0]].edgeCoord
                if newDir=="L":
                    thisSq.adjacent["D"] = (topLeft[0]+ixM,edgeCoord["R"],newDir)
                elif newDir=="R":
                    thisSq.adjacent["D"] = (topLeft[0]+metaSize-ixM-1,edgeCoord["L"],newDir)
                elif newDir=="D":
                    thisSq.adjacent["D"] = (edgeCoord["U"],topLeft[1]+ixM,newDir)
                elif newDir=="U":
                    thisSq.adjacent["D"] = (edgeCoord["D"],topLeft[1]+metaSize-ixM-1,newDir)

# Point to adjacent squares
for iy in range(yDim):
    for ix in range(xDim):
        if grid[iy][ix] is not None:
            for d in dirs:
                adj = grid[iy][ix].adjacent[d]
                if grid[adj[0]][adj[1]].isWall:
                    grid[iy][ix].adjacent[d] = (grid[iy][ix],d)
                else:
                    grid[iy][ix].adjacent[d] = (grid[adj[0]][adj[1]],adj[2])

# Now get onto the instructions!
sq = grid[0][min([ix for ix in range(xDim) if grid[0][ix] is not None])]
heading = 1
ix = 0
while ix<len(instructions):
    ixEnd = ix
    while ixEnd+1<len(instructions) and instructions[ixEnd+1] in digs:
        ixEnd+=1
    moves = int(instructions[ix:ixEnd+1])
    for _ in range(moves):
        adj = sq.adjacent[dirs[heading]]
        sq = adj[0]
        heading = dirs.index(adj[1])
    ix = ixEnd+1
    if ix<len(instructions):
        if instructions[ix]=='L':
            heading = (heading-1)%4
        elif instructions[ix]=='R':
            heading = (heading+1)%4
        ix+=1

        
print((sq.coord[0]+1)*1000+(sq.coord[1]+1)*4+(heading-1)%4)

