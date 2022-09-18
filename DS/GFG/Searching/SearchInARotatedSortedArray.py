#!/usr/bin/python3

arr = list(map(int, (input() or "34 44 56 59 61 87 98 103 3 7 19 23").split()))
target = int(input() or "19")
low = 0
high = arr.__len__() - 1
while low <= high:
    mid = (low+high)//2
    if arr[mid] == target:
        print(mid)
        break
    if arr[mid] > arr[low]: # left half is sorted
        if target >= arr[low] and target < arr[mid]: # Is element lying in the range of (low, mid-1)?
            high = mid-1
        else:
            low = mid+1
    else:
        if target > arr[mid] and target <= arr[high]:
            low = mid+1
        else:
            high = mid-1
else:
    print("-1")
