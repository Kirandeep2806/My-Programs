#!/usr/bin/python3

def Count1sInBinaryArray(arr, n):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == 0:
            low = mid+1
        elif mid!=0 and arr[mid-1]==arr[mid]:
            high = mid-1
        elif arr[mid] == 1:
            return n-mid
    else:
        return 0


arr = list(map(int, (input() or "0 0 1 1 1 1 1").split()))
res = Count1sInBinaryArray(arr, len(arr))
print(res)
