#!/usr/bin/python3

from BinarySearchIterative import binarySearch

arr = list(map(int, input().split()))
targetSum = int(input())
arr.sort()

ptr1 = 0
ptr2 = len(arr)-1

while ptr1<ptr2:
    twoSum = arr[ptr1] + arr[ptr2]
    requiredVal = targetSum - twoSum
    if arr[ptr1] <= requiredVal <= arr[ptr2]:
        res = binarySearch(arr, requiredVal, ptr1+1, ptr2-1)
        if res!=-1:
            print(arr[ptr1], arr[ptr2], arr[res])
            break
    if twoSum > targetSum:
        ptr2 -= 1
    elif twoSum < targetSum:
        ptr1 += 1
    else:
        print("-1")
        break
else:
    print("-1")
