#!/usr/bin/python3

def diceCombinations(n, res, mem={}):
    if n == 0:
        return 0
    if mem.get(n, 0):
        return res+mem[n]
    possibleWays = 0
    for i in range(1, n+1):
        possibleWays += 1
        diceCombinations(n-i)
    mem[n] = possibleWays
    return res+possibleWays

n = int(input())
res = diceCombinations(n, 0)
print(res)
