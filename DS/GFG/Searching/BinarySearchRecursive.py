#!/usr/bin/python3

def binarySearch(arr, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, low, high-1)
    else:
        return binarySearch(arr, target, low+1, high)

arr = list(map(int, input().split()))
target = int(input())
searchRes = binarySearch(arr, target, 0, len(arr)-1)
print(searchRes)
