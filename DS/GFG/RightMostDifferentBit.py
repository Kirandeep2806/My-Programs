#!/usr/bin/python3

import math

n = int(input())
m = int(input())
xor = n^m

if xor == 0:
    print(-1)
else:
    print(int(math.log2(xor&(~(xor-1))))+1)
