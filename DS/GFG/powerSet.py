#!/usr/bin/python3

from math import log2

s = input("Enter a string : ")
n = len(s)

for i in range(2**n):
    res = ''
    while i>0:
        lastSetBit = i&(~(i-1))
        res += s[int(log2(lastSetBit))]
        i = i&(i-1)
    print(res)
