#!/usr/bin/python3

def diceCombinations(n, possibleWays, mem={}):
    if n <= 1:
        return 1
    # if mem.get(n, 0):
    #     return res+mem[n]
    # possibleWays = 0
    for i in range(1, n+1):
        possibleWays += diceCombinations(n-i, possibleWays)
        mem[n] = possibleWays
    # return res+possibleWays

n = int(input() or "3")
res = diceCombinations(n, 0)
print(res)
