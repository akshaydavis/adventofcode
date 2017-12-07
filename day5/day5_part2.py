#------------------Day5-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/5/input
import csv
inputcommands = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/5

def getCommandList(filename):
    commands = [0]
    with open(inputcommands) as inputFile:
        line = inputFile.readline()
        while line:
            commands.extend([int(line)])
            line = inputFile.readline()
    return(commands)

def getCountOfSteps(commandList):
    minPos = 1
    maxPos = len(commandList)
    currentPos = minPos
    steps = 0
    while currentPos >= minPos and currentPos < maxPos:
        nextPos = currentPos + commandList[currentPos]
        if (nextPos - currentPos) > 2:
            commandList[currentPos] = commandList[currentPos] - 1
        else:
            commandList[currentPos] = commandList[currentPos] + 1
        currentPos = nextPos
        steps += 1
    return(steps)

result = getCountOfSteps(getCommandList(inputcommands))

#---------------------------------------#
print("Day 5 Part 2: %d" % result)