#!/usr/bin/env python3

# Trying for partial execution - failed

from math import log2

t = int(input())
for i in range(t):
    length, output = list(map(int, input().split()))
    if length == 1:
        print(output)
        continue
    bitLength = int(log2(output)) + 1
    applyOn = output
    for i in range(length - 1):
        print(1 << bitLength + i, end=" ")
        applyOn = 1 << bitLength+i | applyOn
    print(applyOn)
