#! /usr/bin/python3.8

import sys

allLines = []

for line in sys.stdin:
    allLines.append(line)

def travel(vector, x, y, incX, incY):
    """Tree encounter?"""
    movementRight = (x + incX) % (len(vector[0]) - 1)
    return vector[y + incY][movementRight]

grandTotal = 0

for pair in [(1,1), (3,1), (5,1), (7,1), (1,2)]:

    encounteredTrees = 0
    x = 0
    y = 0

    while y < len(allLines) - pair[1] - 1:
        if travel(allLines, x, y, pair[0], pair[1]) == '#':
            encounteredTrees += 1
        
        x += pair[0]
        y += pair[1]

    if grandTotal == 0:
        grandTotal = encounteredTrees
    else:
        grandTotal *= encounteredTrees

    print(encounteredTrees)


print(grandTotal)

