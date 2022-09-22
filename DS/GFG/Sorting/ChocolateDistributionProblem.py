#!/usr/bin/python3

from sys import maxsize

arr = list(map(int, input().split()))
m = int(input())

arr.sort()
minVal = maxsize
startIndex = 0

for i in range(arr.__len__()-m+1):
    diff = arr[i+m-1] - arr[i]
    if diff < minVal:
        minVal = diff
        startIndex = i

# print(minVal, startIndex)
print(arr[startIndex:startIndex+m], minVal)

