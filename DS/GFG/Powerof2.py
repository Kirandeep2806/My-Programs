#!/usr/bin/python3

n = int(input())
if n == 0:
    print("NO")
elif n&(n-1) == 0:
    print("YES")
else:
    print("NO")
