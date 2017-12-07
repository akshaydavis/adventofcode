#------------------Day4-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/4/input
import csv
inputfile = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/4

def calculateNumberOfValidPassPhrases(input):
    validPassPhrases = 0
    with open(inputfile) as tsv:
        for line in csv.reader(tsv, delimiter=" "):
            #Compare the length of the line with the size of the set to see if it's valid
            if len(line) == len(set(line)):
                validPassPhrases += 1
    return(validPassPhrases)

result = calculateNumberOfValidPassPhrases(inputfile)

#---------------------------------------#
print("Day 4 Part 1: %d" % result)