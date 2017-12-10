#------------------Day10-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/10/input
inputFile = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/10

maxElement = 256
elementlist = [x for x in range(0,maxElement)]
currentPos = 0
skipSize = 0
with open(inputFile) as f:
    lengths = [int(x) for x in f.readline().split(',')]
    for length in lengths:
        sublist = [elementlist[x % maxElement] for x in range(currentPos, currentPos + length)]
        sublist = list(reversed(sublist))
        for x in range(0, length):
            elementlist[(currentPos + x) % maxElement] = sublist[x]
        currentPos = (currentPos + skipSize + length) % maxElement
        skipSize += 1

#---------------------------------------#        
print("Day 10 Part 1: %d" % (elementlist[0] * elementlist[1]))