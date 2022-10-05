#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    maxElement = arr[0]
    index = 0
    for i in range(1, n):
        if arr[i] > maxElement:
            maxElement = arr[i]
            index = i
    if index==0:
        print("-1")
    else:
        print(index)
        print(*arr[:index])
        print(n-index)
        print(*arr[index:])
