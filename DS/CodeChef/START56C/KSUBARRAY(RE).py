#!/usr/bin/python3

from math import gcd

t = int(input())
while t!=0:
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arrGCD = gcd(*arr)
    windowSize = 1
    i = 0
    subArrayGCD = 0
    ptr = i
    while i<n and k!=0:
        if ptr < n:
            if windowSize == 1:
                subArrayGCD = arr[ptr]
            subArrayGCD = gcd(subArrayGCD, arr[ptr])
            if subArrayGCD == arrGCD:
                k -= 1
                windowSize = 1
                i = ptr+1
                ptr = i
            elif subArrayGCD < arrGCD:
                windowSize = 1
                i += 1
                ptr = i
            else:
                windowSize += 1
                ptr += 1
        else:
            i += 1
            ptr = i
            windowSize = 1
    if k == 0:
        print("YES")
    else:
        print("NO")
