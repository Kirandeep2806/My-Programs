#!/usr/bin/python3

def findGCD(a, b):
    if b == 0:
        return a
    else:
        return findGCD(b, a % b)

print(findGCD(12, 8))
