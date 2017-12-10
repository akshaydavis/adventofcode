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
densehash = [0 for x in range(0,16)]
currentPos = 0
skipSize = 0
with open(inputFile) as f:
    lengths = [ord(x) for x in list(f.readline())]
    lengths.extend([17, 31, 73, 47, 23])
    for i in range(0,64):
        for length in lengths:
            sublist = [elementlist[x % maxElement] for x in range(currentPos, currentPos + length)]
            sublist = list(reversed(sublist))
            for x in range(0, length):
                elementlist[(currentPos + x) % maxElement] = sublist[x] 
            currentPos = (currentPos + skipSize + length) % maxElement
            skipSize += 1

for x in range(0,16):
    for i in range(0,16):
        densehash[x] ^= elementlist[i + (16*x)]
    densehash[x] = chr(densehash[x])


#---------------------------------------#
print("Day 10 Part 2: %s" % "".join("{:02x}".format(ord(c)) for c in densehash))