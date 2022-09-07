#!/usr/bin/python3

from collections import Counter

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    removeElements = Counter(list(map(int, input().split())))
    for i in arr:
        if removeElements.get(i, 0) == 0:
            print(i, end=" ")
    print()
