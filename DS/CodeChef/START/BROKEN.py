#!/usr/bin/python3

for i in range(int(input())):
    arr = list(map(int, input().split()))
    if arr[0] > arr[1]:
        print("NEW PHONE")
    elif arr[0] < arr[1]:
        print("REPAIR")
    else:
        print("ANY")
