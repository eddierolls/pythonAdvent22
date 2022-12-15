# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:55:01 2022

@author: edwar
"""
class Sensor(object):
    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius
    
    def findOnRow(self,row):
        distance = abs(row-self.centre[1])
        if self.radius-distance>=0:
            points = (self.centre[0]-(self.radius-distance),self.centre[0]+(self.radius-distance))
        else:
            points = None
        return points

f = open('inputs/Day15.txt')
ROW = 2000000
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
    
ranges = []
for sensor in sensors:
    newRange = sensor.findOnRow(ROW)
    if newRange is not None:
        ranges.append(newRange)

rangeOut = []
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

score = sum([r[1]-r[0]+1 for r in rangeOut]) - sum([b[1]==ROW for b in beacons])
print(score)
