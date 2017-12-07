#------------------Day7-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/7/input
import csv
inputfile = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/7

nodearray = []
rootNode = None
unbalancedNode = None
newNodeWeight = 0

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

def findNode(nodeName):
    foundNode = None
    i = 0
    while nodearray[i].name != nodeName:
        i += 1
    if i < len(nodearray):
        foundNode = nodearray[i]
    return foundNode
    
def recurseSubTreeWeight(nodeName):
    global unbalancedNode
    global newNodeWeight
    weights = []
    weight = 0
    weightdiff = 0
    nodeToChange = None
    subtreeImbalance = False
    thisNode = findNode(nodeName)
    weight = thisNode.weight
    for node in thisNode.above:
        subtreeWeight = recurseSubTreeWeight(node)
        weights.append(subtreeWeight)
        weight+=subtreeWeight
    nodePos = 0
    for nodeWeight in weights:
        if nodeWeight != weights[0]:
            subtreeImbalance = True
            weightdiff = abs(nodeWeight - weights[0])
            nodeToChange = thisNode.above[nodePos]
        nodePos += 1
    if subtreeImbalance and unbalancedNode == None:
        unbalancedNode = nodeToChange
        newNodeWeight = findNode(nodeToChange).weight - weightdiff
    return weight

    
loadNodes(inputfile)
rootNode = findRootNode()        
recurseSubTreeWeight(rootNode)

#---------------------------------------#
print("Day 7 Part 2: \n\tNode: %s \n\tNew Weight: %d" % (unbalancedNode, newNodeWeight))