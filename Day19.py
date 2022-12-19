# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 09:04:24 2022

@author: edwar
"""
from copy import copy
from dataclasses import dataclass

PART2 = True

if PART2:
    MAXTIME = 32
else:
    MAXTIME = 24

class Robot(object):
    def __init__(self,costs,resources):
        self.costs = costs # Ore Clay Obsidian
        self.resources = resources # Ore Clay Obsidian Points

def calcAfford(state,robots):
    afford = [False]*4
    for ixR in range(4):
        if all([state[1][x]>=robots[ixR].costs[x] for x in range(4)]):
            afford[ixR] = True
    return afford

oreTypes = ["ore","clay","obsidian"]

totalScore = []
ixLine = 1
f = open("inputs/Day19.txt")
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
    
    # Prune any states for more of resource X than ever needed
    perMachine = [max([robot.costs[ixC] for robot in robots]) for ixC in range(3)]
    perTime = {t:[perMachine[0]*(MAXTIME-1-t),perMachine[1]*(MAXTIME-1-t),perMachine[2]*(MAXTIME-1-t),99999999999] for t in range(MAXTIME)}

    # Breadth first search is easiest
    nextStates = set([((1,0,0,0),(0,0,0,0))]) # A state is 4 robots then 4 resources. Order is ore, clay, obsidian, score
    for t in range(MAXTIME):
        theseStates = nextStates
        nextStates = set()
        maxIncr = (MAXTIME-t)*(MAXTIME-t+1)/2
        topScore = max([state[1][3]+(state[0][3]*(MAXTIME-t-1)) for state in theseStates])
        for state in theseStates:
            if state[1][3]+state[0][3]*(MAXTIME-t-1)+maxIncr<=topScore:
                continue
            afford = calcAfford(state,robots)
            # Option 1 - do nothing - only if it can't afford all robots
            if not all(afford) or t==MAXTIME-1:
                newResource = [state[1][i]+state[0][i] for i in range(4)]
                newState = (state[0],tuple(newResource))
                nextStates.add(newState)
            # Option 2 - loop through robots to buy
            for ixR in range(4):
                if afford[ixR] and t!=MAXTIME-1 and state[1][ixR]+state[0][ixR]*(MAXTIME-t)<=perTime[t][ixR]:
                    newResource = tuple([state[1][i]+state[0][i]-robots[ixR].costs[i] for i in range(4)])
                    newRobots = list(state[0])
                    newRobots[ixR]+=1
                    nextStates.add((tuple(newRobots),newResource))
        print(ixLine,t,len(nextStates),topScore)
    score = max([state[1][3] for state in nextStates])
    totalScore.append(score)
    ixLine+=1
    if PART2 and ixLine>3:
        break
if PART2 and ixLine==3: # (tests)
    print(totalScore[0]*totalScore[1])
elif PART2: # (tests)
    print(totalScore[0]*totalScore[1]*totalScore[2])
else:
    print(sum([totalScore[i]*(i+1) for i in range(len(totalScore))]))