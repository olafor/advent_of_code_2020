#! /usr/bin/python3.8

import math, sys

def filterRows(s, numRange):
    half = math.ceil(len(numRange) / 2)
    midPoint = numRange[half]
    if s[0] == 'F':
        if len(s) == 1:
            return numRange[0]
        return filterRows(s[1:], list(range(numRange[0], midPoint))) 
    elif s[0] == 'B':
        if len(s) == 1:
            return numRange[1]
        return filterRows(s[1:], list(range(midPoint, numRange[-1] + 1)))

def filterColumns(s, numRange):
    half = math.ceil(len(numRange) / 2)
    midPoint = numRange[half]

    if s[0] == 'L':
        if len(s) == 2:
            return numRange[0]
        return filterColumns(s[1:], list(range(numRange[0], midPoint))) 
    elif s[0] == 'R':
        if len(s) == 2:
            return numRange[1]
        return filterColumns(s[1:], list(range(midPoint, numRange[-1] + 1)))

def getRow(s):
    numRange = list(range(0, 128))
    return filterRows(s, numRange)

def getColumn(s):
    numRange = list(range(0, 8))
    return filterColumns(s, numRange)

def getSeatId(row, column):
    return row * 8 + column

allSeats = []

for line in sys.stdin:
    row = getRow(line[:7])
    column = getColumn(line[7:])
    seatID = getSeatId(row, column)

    allSeats.append(seatID)

allSeats.sort()
print(len(allSeats))

print(allSeats)
