#!/usr/bin/env python3

import math

t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    base = math.log2(n)
    reOccursAt = int(k%base)
    l = [i for i in range(1, n+1)]
    for i in range(reOccursAt):
        l = l[::2] + l[1::2]
    print(*l)
