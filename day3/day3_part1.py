#------------------Day3-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Akshay Davis

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/3/input
target = 277678

#----------------Solution---------------#
# http://adventofcode.com/2017/day/3

#Current size of grid
xlimit = 1
ylimit = 1

#Current position
currentx = 0
currenty = 0

#Position we're moving
incrementx = True  #Moving right
incrementy = False #Moving up
decrementx = False #Moving left
decrementy = False #Moving down
newLayer = True    #Are we expanding the grid

i = 1

while i < target:
    i += 1
    
    if newLayer:
        currentx += 1
        newLayer = False
        incrementx = False
        incrementy = True
    elif incrementy:
        currenty += 1
        if currenty == ylimit:
            incrementy = False
            decrementx = True
    elif decrementx:
        currentx -= 1
        if abs(currentx) == xlimit:
            decrementx = False
            decrementy = True
    elif decrementy:
        currenty -= 1
        if abs(currenty) == ylimit:
            decrementy = False
            incrementx = True
    elif incrementx:
        currentx += 1
        if currentx == xlimit:
            xlimit += 1
            ylimit += 1
            incrementx = False
            newLayer = True

#---------------------------------------#            
distance = abs(currentx) + abs(currenty)
print("Day 3 Part 1: %d" % distance)