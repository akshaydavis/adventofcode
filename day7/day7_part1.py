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
inputfile = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/6
nodearray = []

class Prognode():
    def __init__(self):
        self.name = None
        self.weight = None
        self.above = []
        self.below = None
        
def createNode(nodeString):
    nodeInfo = nodeString.split(' ')
    node = Prognode()
    node.name = nodeInfo[0]
    node.weight = int(nodeInfo[1].strip('()\n'))
    i = 3
    while i < len(nodeInfo):
        node.above.append(nodeInfo[i].strip(',\n'))
        i += 1
    nodearray.append(node)

def loadNodes(filename):
    with open(filename) as inputFile:
        line = inputFile.readline()
        while line:
            createNode(line)
            line = inputFile.readline()
            
def findParent(name):
    parent = None
    for node in nodearray:
        for child in node.above:
            if child == name:
                parent = node.name
                break
        if parent != None:
            break
    return parent
    
def findRootNode():
    rootNode = ''
    for node in nodearray:
        node.below = findParent(node.name)
        if node.below == None:
            rootNode = node.name
            break
    return(rootNode)

loadNodes(inputfile)

result = findRootNode()

#---------------------------------------#
print("Day 7 Part 1: %s" % result)