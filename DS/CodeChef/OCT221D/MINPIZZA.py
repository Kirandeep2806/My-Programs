#!/usr/bin/python3

from math import ceil

for i in range(int(input())):
    a, b = list(map(int, input().split()))
    print(ceil(a*b/4))
