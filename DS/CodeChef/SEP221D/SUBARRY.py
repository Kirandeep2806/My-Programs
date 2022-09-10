#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    minVal = 10**9+1
    minNonAbsVal = minVal
    maxVal = -10**9-1
    maxNonAbsVal = maxVal
    for i in arr:
        minNonAbsVal = min(i, minNonAbsVal)
        minVal = min(abs(i), minVal)
        maxNonAbsVal = max(i, maxNonAbsVal)
        maxVal = max(abs(i), maxVal)
    print(min(minVal**2, minNonAbsVal*maxNonAbsVal), maxVal**2)
