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
    with open(input) as tsv:
        for line in csv.reader(tsv, delimiter=" "):
            #Create an array of sorted words.
            #This can be compared to each other to determine anagrams
            sortedwords = [''.join(sorted(word)) for word in line]
            if len(line) == len(list(set(sortedwords))):
                validPassPhrases += 1
    return(validPassPhrases)
    
result = calculateNumberOfValidPassPhrases(inputfile)

#---------------------------------------#
print("Day 4 Part 2: %d" % result)