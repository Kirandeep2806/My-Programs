#!/usr/bin/python3

def lastOccurenceIndex(arr, target, low, high):
    n = len(arr)
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target and mid == n-1:
            return mid
        elif arr[mid] == target and arr[mid] != arr[mid+1]:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    else:
        return -1

if __name__ == '__main__':
    arr = list(map(int, (input() or "1 1 10 10 10 20 20 40").split()))
    target = int(input())
    res = lastOccurenceIndex(arr, target, 0, len(arr)-1)
    print(res)
