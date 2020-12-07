#! /usr/bin/python3.8

import sys, string

grandTotal = 0

checksDict = dict.fromkeys(string.ascii_lowercase, False)

for line in sys.stdin:
    if line == '\n':
        grandTotal += sum(value == True for value in checksDict.values())
        checksDict = dict.fromkeys(checksDict, False)

    for key in checksDict:
        if key in line:

            checksDict[key] = True

grandTotal += sum(value == True for value in checksDict.values())
print(grandTotal)
