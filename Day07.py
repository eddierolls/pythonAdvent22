# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:31:55 2022

@author: edwar
"""

class Node(object):
    def __init__(self,name,parent):
        self.name = name
        self.childrenDir = []
        self.parent = parent
        self.childrenLeaf = {}

    def calcScore(self,allNodes):
        score = 0
        for childrenDir in self.childrenDir:
            score+=allNodes[childrenDir].calcScore(allNodes)
        score+=sum(list(self.childrenLeaf.values()))
        return score

f = open('inputs/Day07.txt')

thisNode = None
allNodes = {}
for line in f:
    line = line.strip()
    if line=="$ cd /":
        thisNode = Node('/',None)
        allNodes["/"] = thisNode
    elif line=="$ cd ..":
        thisNode = thisNode.parent
    elif line[:4]=="$ cd":
        nodeName = thisNode.name+'/'+line.split(' ')[2]
        if nodeName in allNodes:
            thisNode = allNodes[nodeName]
        else:
            thisNode = Node(nodeName,thisNode)
            allNodes[nodeName] = thisNode
    elif line=="$ ls":
        pass # Pretty sure this is safe to skip
    elif line[:3]=="dir":
        nodeName = thisNode.name+'/'+line.split(" ")[1]
        if nodeName not in allNodes:
            allNodes[nodeName] = Node(nodeName,thisNode)
        thisNode.childrenDir.append(nodeName)
    else:
        (size,leafName) = line.split(' ')
        thisNode.childrenLeaf[leafName] = int(size)

fullScore = 0
for node in allNodes.keys():
    thisScore = allNodes[node].calcScore(allNodes)
    allNodes[node].score = thisScore
    if thisScore<=100000:
        fullScore+=thisScore
print(fullScore)

totalSpace = 70000000
unusedNeeded = 30000000
currentSpace = allNodes['/'].score
bestScore = totalSpace
for node in allNodes.keys():
    thisScore = allNodes[node].score
    if currentSpace-thisScore<=totalSpace-unusedNeeded and thisScore<bestScore:
        bestScore = thisScore

print(bestScore)
