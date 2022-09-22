#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    nonNegative = 0
    hasZero = False
    l = list(map(int, input().split()))
    for i in l:
        if i == 0:
            hasZero = True
            break
        if i<0:
            nonNegative += 1
    if hasZero or nonNegative&1 == 0:
        print("0")
    else:
        print("1")
