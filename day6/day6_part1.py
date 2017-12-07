#------------------Day6-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/6/input
import csv
inputmemory = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/6

seenstates = []

def loadInitialState(filename):
    memorystate = []
    with open(filename) as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            memorystate = [int(numeric_string) for numeric_string in line]
    return(memorystate)

def findStartPos():
    startPos = 0
    i = 0
    while i < len(memorystate):
        if memorystate[i] > memorystate[startPos]:
            startPos = i
        i += 1
    return startPos

def redistributeMemory(startPos):
    toRedistribute = memorystate[startPos]
    memorystate[startPos] = 0
    currentPos = (startPos + 1) % len(memorystate)
    while toRedistribute > 0:
        memorystate[currentPos] = memorystate[currentPos] + 1
        toRedistribute -= 1
        currentPos = (currentPos + 1) % len(memorystate)

def checkIfSeenBeforeOrAdd():
    seenBefore = False
    memoryString = ','.join([str(val) for val in memorystate])
    seenstates.append(memoryString)
    if len(seenstates) > len(set(seenstates)):
        seenBefore = True
    return seenBefore

memorystate = loadInitialState(inputmemory)

#Add the initial memory state
seenBefore = checkIfSeenBeforeOrAdd()

loops = 0
while not seenBefore:
    redistributeMemory(findStartPos())
    seenBefore = checkIfSeenBeforeOrAdd()
    loops += 1

#---------------------------------------#
print("Day 6 Part 1: %d" % loops)