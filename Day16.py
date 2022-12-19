# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 20:50:48 2022

@author: edwar
"""
from copy import copy
import heapq

class Valve(object):
    def __init__(self,name,flow):
        self.name = name
        self.flow = flow
        self.adjacent = []
        self.distances = {}
        
    def populateDistances(self):
        visited = set([self.name])
        distance = 0
        nextVisit = set(self.adjacent)
        while len(nextVisit)>0:
            thisVisit = nextVisit
            nextVisit = set()
            distance+=1
            for v in thisVisit:
                if v.name not in visited:
                    visited.add(v.name)
                    nextVisit = nextVisit.union(set(v.adjacent))
                    if v.flow>0:
                        self.distances[v.name] = distance

class State(object):
    def __init__(self,timeLeft,currentValve,score,visited,flowDict=None,minDist=None):
        self.timeLeft = timeLeft
        self.currentValve = currentValve
        self.score = score
        self.visited = visited
        if type(self.timeLeft)==list:
            self.bestScore = self.maxScore(flowDict,minDist)
        
    
    def maxScore(self,flowDict,minDist):
        s1,s2 = sorted(self.timeLeft)
        maxScore = self.score
        notVisited = set(flowDict.keys()).difference(self.visited)
        notVisited = sorted([flowDict[v] for v in notVisited],reverse=True)
        ix=0
        while s2>minDist+1 and ix<len(notVisited):
            s2-=(minDist+1)
            maxScore+=s2*notVisited[ix]
            ix+=1
            s1,s2 = sorted([s1,s2])
        return maxScore
    
    def __lt__(self,other):
        return self.bestScore>other.bestScore
            
            
allValves = {}
flowValves = set()
f = open("inputs/Day16.txt")
for line in f:
    line = line.strip().split("Valve ")[1]
    name = line.split(" has")[0]
    flow = int(line.split("=")[1].split(";")[0])
    thisValve = Valve(name,flow)
    allValves[name] = thisValve
    if flow>0:
        flowValves.add(thisValve.name)
    tunnels = line.split("valve")[1].strip('s ').split(', ')
    for t in tunnels:
        if t in allValves.keys():
            thisValve.adjacent.append(allValves[t])
            allValves[t].adjacent.append(thisValve)

minDist = 9
for valve in flowValves:
    allValves[valve].populateDistances()
    minDist = min(minDist,min(allValves[valve].distances.values()))
print(minDist)
allValves["AA"].populateDistances()


# Part A
stack = [State(30,"AA",0,set())]
topScore = 0
while len(stack)>0:
    thisState = stack.pop()
    for nextValve in flowValves.difference(thisState.visited):
        timeLeft = thisState.timeLeft-allValves[thisState.currentValve].distances[nextValve]-1
        if timeLeft>0:
            visited = copy(thisState.visited)
            visited.add(nextValve)
            score = thisState.score + timeLeft*allValves[nextValve].flow
            nextState = State(timeLeft,nextValve,score,visited)
            stack.append(nextState)
            topScore = max(score,topScore)

print(topScore)
            
# Part B
stack = []
flowDict = {v:allValves[v].flow for v in flowValves}
heapq.heappush(stack,State([26,26],["AA","AA"],0,set(),flowDict,minDist))
topScore = 0
while len(stack)>0:
    thisState = heapq.heappop(stack)
    if thisState.bestScore<=topScore:
        break
    for nextValve in flowValves.difference(thisState.visited):
        toMove = int(thisState.timeLeft[1]>thisState.timeLeft[0])
        timeLeft = copy(thisState.timeLeft)
        timeLeft[toMove] = thisState.timeLeft[toMove]-allValves[thisState.currentValve[toMove]].distances[nextValve]-1
        if timeLeft[toMove]>0:
            visited = copy(thisState.visited)
            visited.add(nextValve)
            score = thisState.score + timeLeft[toMove]*allValves[nextValve].flow
            currentValve = copy(thisState.currentValve)
            currentValve[toMove] = nextValve
            nextState = State(timeLeft,currentValve,score,visited,flowDict,minDist)
            heapq.heappush(stack,nextState)
            if topScore<score:
                topScore=max(topScore,score)
                print(topScore,len(stack))

print(topScore)
