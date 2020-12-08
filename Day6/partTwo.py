#! /usr/bin/python3.8

import sys, string

grandTotal = 0
checksDict = dict.fromkeys(string.ascii_lowercase, 0)
groupCount = 0

for line in sys.stdin:
    if line == '\n':
        grandTotal += sum(value == groupCount for value in checksDict.values())
        checksDict = dict.fromkeys(checksDict, 0)
        groupCount = 0
    else:
        for key in checksDict:
            if key in line:
                checksDict[key] += 1 
        groupCount += 1

grandTotal += sum(value == groupCount for value in checksDict.values())
print(grandTotal)
