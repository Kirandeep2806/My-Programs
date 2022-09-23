#!/usr/bin/python3

from math import ceil

for i in range(int(input())):
    l, k = list(map(int, input().split()))
    if l%k == 0:
        print(0)
    else:
        print(1)
