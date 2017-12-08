#------------------Day8-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/8/input
import operator

inputfile = "input.txt"

#----------------Solution---------------#
# http://adventofcode.com/2017/day/8

registers = {}
highestval = 0
operators = { "<": operator.lt, ">": operator.gt, "==": operator.eq, ">=": operator.ge, "<=": operator.le, "!=": operator.ne, "inc": operator.add, "dec": operator.sub }

def testCondAndApplyUpdate(testRegister, applyRegister, incdec, applyValue, testValue, testCond):
    global registers
    if testRegister not in registers: registers[testRegister] = 0
    if applyRegister not in registers: registers[applyRegister] = 0
    if operators[testCond](registers[testRegister],testValue): registers[applyRegister] = operators[incdec](registers[applyRegister], applyValue)
    
def processInstruction(instruction):
    global highestval
    commands = instruction.split(' ')
    testCondAndApplyUpdate(commands[4], commands[0], commands[1], int(commands[2]), int(commands[6].strip('\n')), commands[5])
    if registers[commands[0]] > highestval: highestval = registers[commands[0]]
    
with open(inputfile) as inputFile:
    line = inputFile.readline()
    while line:
        processInstruction(line)
        line = inputFile.readline()

maxVal = -999
for key, value in registers.items():
    if value > maxVal:
        maxVal = value

#---------------------------------------#
print("Day 8 Part 1: %d" % maxVal)
print("Day 8 Part 2: %d" % highestval)