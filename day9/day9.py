#------------------Day9-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/9/input
inputfile = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/2

rootNode = None
garbageCount = 0
class streamGroup():
    def __init__(self):
        self.children = []
        self.parent = None
        
with open(inputfile) as f:
    inGarbage = False
    currentNode = None
    c = f.read(1)
    currentNode = streamGroup()
    rootNode = currentNode
    while c:
        c = f.read(1)
        if c == "!":
            c = f.read(1)
        elif c == "<" and not inGarbage:
            inGarbage = True
        elif c == ">" and inGarbage:
            inGarbage = False
        elif c == "{" and not inGarbage:
            currentNode.children.append(streamGroup())
            currentNode.children[len(currentNode.children)-1].parent = currentNode
            currentNode = currentNode.children[len(currentNode.children)-1]
        elif c == "}" and not inGarbage:
            currentNode = currentNode.parent
        elif inGarbage:
            garbageCount += 1

def recurseAndCountNodes(node, depth):
    currentDepth = depth + 1
    score = currentDepth
    for child in node.children:
        score += recurseAndCountNodes(child, currentDepth)
    return score

#---------------------------------------#
print("Day 9 part 1: %d" % recurseAndCountNodes(rootNode,0))
print("Day 9 part 2: %d" % garbageCount)