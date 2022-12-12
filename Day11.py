# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:49:00 2022

@author: edwar
"""
WORRYFACTOR = 1
ROUNDS = 10000
from time import time

def extractAfter(s,txt):
    return s.strip().split(txt)[1]

class Monkey(object):
    def __init__(self,monkeyId):
        self.inspections = 0
        self.id=monkeyId
    
    def interpretStartingItems(self,line):
        line = extractAfter(line,"Starting items: ")
        self.items = list(map(int,line.split(", ")))
        
    def interpretOperation(self,line):
        line = extractAfter(line,"Operation: new = old ")
        if line=="* old":
            self.operation = [0,0,1]
        elif line[0]=="*":
            self.operation = [0,int(line[1:]),0]
        elif line[0]=="+":
            self.operation = [int(line[1:]),1,0]
        else:
            ValueError("Line not recognised")
    
    def interpretTest(self,line):
        line = extractAfter(line,"Test: divisible by ")
        self.test = int(line)
        
    def interpretSendTo(self,line1,line2):
        line1 = extractAfter(line1,"If true: throw to monkey ")
        line2 = extractAfter(line2,"If false: throw to monkey ")
        self.sendTo = [int(line2),int(line1)]

# Initialize
clocktime = time()
f = open('inputs/Day11.txt')
monkeyList = []
monkeyId = 0
while f.readline()!='': # EOF
    thisMonkey = Monkey(monkeyId)
    thisMonkey.interpretStartingItems(f.readline())
    thisMonkey.interpretOperation(f.readline())
    thisMonkey.interpretTest(f.readline())
    thisMonkey.interpretSendTo(f.readline(),f.readline())
    monkeyList.append(thisMonkey)
    monkeyId+=1
    f.readline()

DIVFACTOR = 1
for monkey in monkeyList:
    DIVFACTOR*=monkey.test

# Play
for t in range(ROUNDS):
    for monkey in monkeyList:
        while len(monkey.items)>0:
            item = monkey.items.pop()            
            monkey.inspections+=1
            item = sum([monkey.operation[i]*(item**i) for i in range(3)])
            item = item//WORRYFACTOR
            item%=DIVFACTOR
            nextMonkey = monkey.sendTo[(item%monkey.test)==0]
            monkeyList[nextMonkey].items.append(item)

inspectionList = list(sorted([monkey.inspections for monkey in monkeyList],reverse=True))
print(inspectionList[0]*inspectionList[1])
print(time()-clocktime)
