#!/bin/usr/env python3

def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr


arr = list(map(int, input("Enter the numbers : ").split()))
sorted_arr =  selectionSort(arr)

print("Sorted array :", sorted_arr)
