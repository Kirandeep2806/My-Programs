#!/usr/bin/python3

def binarySearch(arr, target, low, high):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target and mid == len(arr)-1:
            return mid
        elif arr[mid] == target and arr[mid] != arr[mid+1]:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    else:
        return -1

arr = list(map(int, (input() or "1 1 10 10 10 20 20 40").split()))
target = int(input())
res = binarySearch(arr, target, 0, len(arr)-1)
print(res)
