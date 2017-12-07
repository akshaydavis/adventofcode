#------------------Day2-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/2/input
import csv
inputFile = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/2

def calculateChecksum(filename):
    checksum = 0
    with open(inputFile) as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            numericArr = [int(numeric_string) for numeric_string in line]
            numericArr.sort()
            rowdiff = numericArr[len(numericArr) - 1] - numericArr[0]
            checksum += rowdiff
    return(checksum)

result = calculateChecksum(inputFile)
#---------------------------------------#
print('Day 2 Part 1: %d' % result)