#! /usr/bin/python3.8

import sys

# "cid" is optional - ignore
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

checksDict = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False
        }

numberOfValidPassports = 0

for line in sys.stdin:
    if line == '\n':
        checksDict = dict.fromkeys(checksDict, False)

    for key in checksDict:
        if key in line:
            checksDict[key] = True

    if all(key == True for key  in checksDict.values()):
        numberOfValidPassports += 1
        checksDict = dict.fromkeys(checksDict, False)

print(numberOfValidPassports)


