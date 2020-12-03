#! /usr/bin/python3.8

import sys

allLines = []

for line in sys.stdin:
    allLines.append(line)

def travel(vector, x, y):
    """Tree encounter?"""
    movementRight = (x + 3) % (len(vector[0]) - 1)
    return vector[y+1][movementRight]

encounteredTrees = 0
x = 0
y = 0

while y < len(allLines) - 2:
    if travel(allLines, x, y) == '#':
        encounteredTrees += 1
    
    x += 3
    y += 1

print(encounteredTrees)

