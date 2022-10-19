#!/usr/bin/python3

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    l1 = input()
    l2 = input()
    d1 = Counter(l1)
    d2 = Counter(l2)
    maxVal = 0
    for i in d1:
        maxVal = max(min(d1[i], d2[i]), maxVal)
    print(maxVal)
