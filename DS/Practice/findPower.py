#!/usr/bin/python3

def fastPower(a, b):
    res = 1
    while b:
        if b&1:
            res = res*a
        a = a*a
        b = b>>1
    return res

print(fastPower(2, 2))
