#!/usr/bin/python3

from math import log2, ceil
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = Counter(l)
    maxVal = 0
    for i in d:
        maxVal = max(maxVal, d[i])
    print(ceil(log2(maxVal)))
