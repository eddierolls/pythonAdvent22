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
        points = set([(x+self.centre[0],row) for x in range(distance-self.radius,self.radius-distance+1)])
        return points

f = open('inputs/Day15.txt')
ROW = 2000000
overlap = set()
sensors = []
beacons = set()
for line in f:
    line = line.strip().split("Sensor at x=")[1]
    centre = (int(line.split(',')[0]),int(line.split(', y=')[1].split(':')[0]))
    line = line.split("closest beacon is at x=")[1]
    beacon = tuple(map(int,line.split(", y=")))
    radius = abs(beacon[0]-centre[0]) + abs(beacon[1]-centre[1])
    sensors.append(Sensor(centre,radius))
    beacons.add(beacon)

overlap = set()
for sensor in sensors:
    overlap = overlap.union(sensor.findOnRow(ROW))
    print(sensor.centre)

print(len(overlap.difference(beacons)))
