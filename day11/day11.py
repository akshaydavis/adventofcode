#------------------Day11-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/11/input
import operator

inputfile = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/4

coord = [0,0,0]
maxDistance = 0
coordchange = {"n": [0,1,-1], "s": [0,-1,1], "ne": [1, 0, -1], "se": [1, -1, 0], "nw": [-1, 1, 0], "sw": [-1, 0, 1]}

def currentDistance():
    return int((abs(coord[0]) + abs(coord[1]) + abs(coord[2])) / 2)

with open(inputfile) as f:
    steps = f.read().split(',')
    for step in steps:
        coord = list(map(operator.add, coord, coordchange[step]))
                
        if maxDistance < currentDistance():
            maxDistance = currentDistance()

#---------------------------------------#            
print("Day 11 Part 1: %d" % currentDistance())
print("Day 11 Part 2: %d" % maxDistance)