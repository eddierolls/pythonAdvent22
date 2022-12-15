# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:55:01 2022

@author: edwar
"""
from itertools import permutations

ROW = 2000000
MAXCOORD = 4000000
#ROW = 10
#MAXCOORD = 20

class Sensor(object):
    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius
    
    def findOnRow(self,row,dim=0):
        distance = abs(row-self.centre[1-dim])
        if self.radius-distance>=0:
            points = (self.centre[dim]-(self.radius-distance),self.centre[dim]+(self.radius-distance))
        else:
            points = None
        return points

def makeRowCalculations(sensors,row):
    ranges = []
    for sensor in sensors:
        newRange = sensor.findOnRow(row)
        if newRange is not None:
            ranges.append(newRange)
    
    rangeOut = []
    minOverlap = MAXCOORD
    for r1 in ranges:
        ix=0
        while ix<len(rangeOut):
            r2 = rangeOut[ix]
            if r1[1]>=r2[0] and r1[0]<=r2[1]:
                r1 = (min(r1[0],r2[0]),max(r1[1],r2[1]))
                rangeOut.remove(r2)
            else:
                ix+=1
        rangeOut.append(r1)
    rangeScore = sum([r[1]-r[0]+1 for r in rangeOut])
    
    for r1,r2 in permutations(ranges,2):
        if r1[1]>=r2[0] and r1[0]<=r2[1]:
            if (r1[1]>=r2[1] and r1[0]<=r2[0]):
                thisOverlap = r1[1]-r1[0]
            elif (r1[1]<=r2[1] and r1[0]>=r2[0]):
                thisOverlap = r2[1]-r2[0]
            else:
                thisOverlap = min(r1[1]-r2[0],r2[1]-r1[0])
            minOverlap = min(thisOverlap,minOverlap)
        if minOverlap==0:
            break
    return rangeScore,rangeOut,minOverlap


f = open('inputs/Day15.txt')
overlap = set()
sensors = []
beacons = set()
score = 0
for line in f:
    line = line.strip().split("Sensor at x=")[1]
    centre = (int(line.split(',')[0]),int(line.split(', y=')[1].split(':')[0]))
    line = line.split("closest beacon is at x=")[1]
    beacon = tuple(map(int,line.split(", y=")))
    radius = abs(beacon[0]-centre[0]) + abs(beacon[1]-centre[1])
    sensors.append(Sensor(centre,radius))
    beacons.add(beacon)
    
rowScore,_,_ = makeRowCalculations(sensors,ROW)

score = rowScore - sum([b[1]==ROW for b in beacons])
print(score)

row = 2700000
found = False
while not found and row<MAXCOORD:
    _,rangeOut,minOverlap = makeRowCalculations(sensors,row)
    if len(rangeOut)>1:
        print((min(rangeOut[0][1],rangeOut[1][1])+1)*4000000+row)
        found = True
    else:
        row+=(1+minOverlap//2)
    if (row%10000)==0:
        print(row)
    if minOverlap>0:
        print(row)
        

