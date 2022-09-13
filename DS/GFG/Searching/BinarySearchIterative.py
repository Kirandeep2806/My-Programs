#!/usr/bin/python3

def binarySearch(arr, target, low, high):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    else:
        return -1

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    searchRes = binarySearch(arr, target, 0, len(arr)-1)
    print(searchRes)
