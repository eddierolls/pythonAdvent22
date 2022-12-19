# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 09:04:25 2022

@author: edwar
"""
ALLDIR = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

def isInsideGrid(cube,maxDim):
    inside = True
    for ind in range(3):
        if cube[ind]<-1 or cube[ind]>maxDim[ind]+1:
            inside = False
    return inside
    

def findAllOutside(cubes):
    maxDim = tuple(map(lambda x:max([c[x] for c in cubes]),list(range(3))))
    outside = set((0,0,0))
    stack = [(0,0,0)]
    while len(stack)>0:
        cube = stack.pop()
        for adj in ALLDIR:
            adjCube = tuple([cube[i]+adj[i] for i in range(3)])
            if adjCube not in outside and isInsideGrid(adjCube,maxDim) and adjCube not in cubes:
                outside.add(adjCube)
                stack.append(adjCube)
    return outside


f = open("inputs/Day18.txt")
cubeSet = set()
score = 0
for line in f:
    newCube = tuple(map(int,line.strip().split(',')))
    cubeSet.add(newCube)

outsideCubes = findAllOutside(cubeSet)
scoreA = 0
scoreB = 0
for c in cubeSet:
    for adj in ALLDIR:
        adjCube = tuple([c[i]+adj[i] for i in range(3)])
        if adjCube in outsideCubes:
            scoreA+=1
            scoreB+=1
        elif adjCube not in cubeSet:
            scoreA+=1

print(scoreA,scoreB)
    
