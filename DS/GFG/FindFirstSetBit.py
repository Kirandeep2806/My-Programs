#!/usr/bin/python3

from math import log2

n = int(input())
if n==0:
    print(0)
else:
    print(int(log2(n&(~(n-1))))+1)
