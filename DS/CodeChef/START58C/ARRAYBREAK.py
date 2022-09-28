#!/usr/bin/python3

for _ in range(int(input())):
    odd = 0
    n = int(input())
    l = list(map(int, input().split()))
    for i in l:
        if i&1:
            odd += 1
    even = n - odd
    if even == n or odd == n:
        print(0)
    else:
        print(even)
