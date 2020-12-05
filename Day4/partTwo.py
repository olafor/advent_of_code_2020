#! /usr/bin/python3.8

import sys

eyeColour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkHex(s):
    for i in range(len(s)):
        if ('0' > s[i] or '9' < s[i]) and ('a' > s[i] or 'f' < s[i]):
            return False
        else:
            return True

def checkValidity(key, value):
    if key == "byr":
        return 1920 <= int(value) <= 2002
    if key == "iyr":
        return 2010 <= int(value) <= 2020
    if key == "eyr":
        return 2020 <= int(value) <= 2030
    if key == "hgt":
        if value[-2:] == "cm":
            return 150 <= int(value[:-2]) <= 193
        if value[-2:] == "in":
            return 59 <= int(value[:-2]) <= 76
        else:
            return False
    if key == "hcl":
        return value[0] == '#' and len(value[1:]) == 6 and checkHex(value[1:])
    if key == "ecl":
        if value in eyeColour:
            return True
        else:
            return False
    if key == "pid":
        return len(value) == 9 and value.isdigit() 
    else:
        return False

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

    words = line.split()

    for word in words:
        for key in checksDict:
            if key in word:
                k,v = word.split(':')
                if checkValidity(k, v) == True:
                    checksDict[key] = True
                else:
                    break

    if all(key == True for key  in checksDict.values()):
        numberOfValidPassports += 1
        checksDict = dict.fromkeys(checksDict, False)

print(numberOfValidPassports)


