#!/usr/bin/python3

def checkCombis(arr):
    distinctStill = 0
    if arr[0] > 0:
        distinctStill += 1
    if arr[1] > 0:
        distinctStill += 1
    if arr[2] > 0:
        distinctStill += 1
    return distinctStill

t = int(input())
while t>0:
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    defaultDistinct = 0
    res = 0
    if arr[0] > 0:
        defaultDistinct += 1
    if arr[1] > 0:
        defaultDistinct += 1
    if arr[2] > 0:
        defaultDistinct += 1
    otherCombinations = 0
    for i in range(3):
        for j in range(i+1, 3):
            if arr[i]!=0 and arr[j]!=0:
                otherCombinations += 1
                arr[i] -= 1
                arr[j] -= 1
                res = max(checkCombis(arr) + otherCombinations, res)
    print(max(res, defaultDistinct))
    t -= 1
