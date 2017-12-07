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
    with open(filename) as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            numericArr = [int(numeric_string) for numeric_string in line]
            numericArr.sort()
            i = 0
            rowdiff = -1
            while i < len(numericArr) and rowdiff < 0:
                j = i + 1
                while j < len(numericArr) and rowdiff < 0:
                    if (numericArr[j] % numericArr[i]) == 0:
                        rowdiff = numericArr[j] / numericArr[i]
                    j += 1
                i += 1
            checksum += rowdiff
    return(checksum)
    
result = calculateChecksum(inputFile)
#---------------------------------------#
print('Day 2 Part 2: %d' % result)