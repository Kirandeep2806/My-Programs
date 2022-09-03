#!/usr/bin/python3

arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        if arr[i] != arr[0]:
            print("From ", i, "-", end="", sep="")
        else:
            print(i-1)
        
if arr[len(arr)-1] != arr[0]:
    print(i)
