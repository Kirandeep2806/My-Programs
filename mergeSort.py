#!/usr/bin/env python3

def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high)//2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, high, mid)
    return arr

def merge(arr, low, high, mid):
    res, i, j = [], low, mid+1
    while i<=mid and j<=high:
        if arr[i] < arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1
    while i<=mid:
        res.append(arr[i])
        i += 1
    while j<=high:
        res.append(arr[j])
        j += 1
    for k in range(len(res)):
        arr[low+k] = res[k]

n = list(map(int, input("Enter input : ").split()))
temp = mergeSort(n, 0, len(n)-1)
print("Sorted array :", *temp)
