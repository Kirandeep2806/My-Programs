#!/usr/bin/python3

from IndexOfFirstOccurenceInSorted import firstOccurenceIndex
from IndexOfLastOccurenceInSorted import lastOccurenceIndex

def countOccurences(arr, target, low, high):
    startIndex = firstOccurenceIndex(arr, target, low, high)
    if startIndex == -1:
        return 0
    endIndex = lastOccurenceIndex(arr, target, low, high)
    return endIndex - startIndex + 1

arr = list(map(int, (input() or "1 1 10 10 10 20 40").split()))
target = int(input())
res = countOccurences(arr, target, 0, len(arr)-1)
print(res)
