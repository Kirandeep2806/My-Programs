#!/usr/bin/python3

from collections import Counter
from math import factorial as f

def getCombinationCount(n):
    return f(n)//(2*f(n-2))


for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    res = 0
    for i in freq:
        if freq[i] >= 2:
            res += getCombinationCount(freq[i])
    print(res)
