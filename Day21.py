# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 19:45:58 2022

@author: edwar
"""

class Monkey(object):
    def __init__(self,name,operation,children,score):
        self.name = name
        self.operation = operation
        self.children = children
        self.score = score
        self.humanRoot = None
    
    def getScore(self):
        if self.children is None:
            return self.score
        else:
            self.score = runOperation(self.children[0].getScore(),self.children[1].getScore(),self.operation)
            return self.score
        
    def getHumanRoot(self):
        if self.name=="humn":
            self.humanRoot = True
        elif self.children is None:
            self.humanRoot = False
        else:
            self.children[0].getHumanRoot()
            self.children[1].getHumanRoot()
            if self.children[0].humanRoot or self.children[1].humanRoot:
                self.humanRoot = True
            else:
                self.humanRoot = False
        return self.humanRoot

def runOperation(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    else:
        raise ValueError("Operand not recognised")

def reverseOperation(target,other,ixH,op):
    if op=="+":
        return target-other
    elif op=="-" and ixH==0:
        return target+other
    elif op=="-" and ixH==1:
        return other-target
    elif op=="*":
        return target/other
    elif op=="/" and ixH==0:
        return target*other
    elif op=="/" and ixH==1:
        return other/target
    else:
        raise ValueError("Operand not recognised")

f = open("inputs/Day21.txt")
monkeyDict = {}
operands = ['+','-','*','/']

for line in f:
    line = line.strip()
    name = line.split(':')[0]
    if any([o in line for o in operands]):
        children = (line.split(' ')[1],line.split(' ')[3])
        operation = line.split(' ')[2]
        score = 0
    else:
        children = None
        operation = None
        score = int(line.split(' ')[1])
    monkey = Monkey(name,operation,children,score)
    monkeyDict[name] = monkey

for monkey in monkeyDict.values():
    if monkey.children:
        monkey.children = (monkeyDict[monkey.children[0]],monkeyDict[monkey.children[1]])

# Part 1
print(monkeyDict["root"].getScore())

# Part 2
monkeyDict["root"].getHumanRoot()

monkey = monkeyDict["root"]
ixH = int(monkey.children[1].humanRoot)
currScore = monkey.children[1-ixH].score
monkey = monkey.children[ixH]
while monkey.name!="humn":
    ixH = int(monkey.children[1].humanRoot)
    currScore = reverseOperation(currScore,monkey.children[1-ixH].score,ixH,monkey.operation)
    monkey = monkey.children[ixH]

print(currScore)
