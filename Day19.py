# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 09:04:24 2022

@author: edwar
"""
from copy import copy
from dataclasses import dataclass

class Robot(object):
    def __init__(self,costs,resources):
        self.costs = costs # Ore Clay Obsidian
        self.resources = resources # Ore Clay Obsidian Points

@dataclass(frozen=True)
class State(object):
    def __init__(self,robots,resources):
        object.__setattr__(self,"robots",robots)
        object.__setattr__(self,"resources",resources) # Ore Clay Obsidian Points
    
    def calcAfford(self,robots):
        afford = [False]*4
        for ixR in range(4):
            if all([self.resources[x]>=robots[ixR].costs[x] for x in range(4)]):
                afford[ixR] = True
        return afford

    def __eq__(self,other):
        return self.robots==other.robots and self.resources==other.resources

oreTypes = ["ore","clay","obsidian"]

f = open("tests/Day19.txt")
for line in f:
    line = line.strip().split('.')
    robots = []
    for ixR in range(4):
        thisLine = line[ixR].split('costs')[1]
        costs = [0,0,0,0]
        resources = tuple([int(x==ixR) for x in range(4)])
        for ixO in range(len(oreTypes)):
            ore = oreTypes[ixO]
            if ore in thisLine:
                oreCount = int(thisLine.split(ore)[-2].split(' ')[-2])
                costs[ixO] = oreCount
        newRobot = Robot(tuple(costs),resources)
        robots.append(newRobot)
    
    # Breadth first search is easiest
    nextStates = set([State((1,0,0,0),(0,0,0,0))])
    for t in range(24):
        theseStates = nextStates
        nextStates = set()
        for state in theseStates:
            afford = state.calcAfford(robots)
            # Option 1 - do nothing - only if it can't afford all robots
            if not all(afford):
                newResource = tuple([state.resources[i]+state.robots[i] for i in range(4)])
                newState = State(state.robots,newResource)
                nextStates.add(newState)
            # Option 2 - loop through robots to buy
            for ixR in range(4):
                if afford[ixR]:
                    newResource = tuple([state.resources[i]+state.robots[i]-robots[ixR].costs[i] for i in range(4)])
                    newRobots = list(state.robots)
                    newRobots[ixR]+=1
                    nextStates.add(State(tuple(newRobots),newResource))
        topState = max([state.resources[2] for state in nextStates])
        print(t,len(nextStates),topState)