#!/usr/bin/python3

from BinarySearchIterative import binarySearch

arr = list(map(int, input().split())) # Input should be a sorted array
target = int(input())
i = 1
res = 0
if arr[res] == target:
    print(res)
else:
    while True:
        if arr[i] == target:
            res = i
            break
        elif arr[i] > target:
            res = binarySearch(arr, target, i//2+1, i-1)
            break
        i <<= 1
    if res != -1:
        print(res)
    else:
        print("Not Found")
