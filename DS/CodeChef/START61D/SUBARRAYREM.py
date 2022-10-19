#!/usr/bin/python3

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = Counter(l)
    res = 0
    if c[1]>c[0]:
        res+=c[0]
        c[1]-=c[0]
        c[0]=0
    else:
        res+=c[1]
        c[0]-=c[1]
        c[1]=0
    res+=(c[1]//3)
    print(res)
