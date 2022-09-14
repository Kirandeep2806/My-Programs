#!/usr/bin/python3

from math import ceil

t = int(input())
while t > 0:
    res = 0
    n, m = list(map(int, input().split()))
    half = ceil(m/2)
    for i in list(map(int, input().split())):
        if i<=half:
            res += m-i
        else:
            res += i-1
    t -= 1
    print(res)
