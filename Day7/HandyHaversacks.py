#! /usr/bin/python3.8

import sys

def parseString(raw):
    container, rest = raw.split(" bags contain ")
    
    if "no other bags." in rest:



