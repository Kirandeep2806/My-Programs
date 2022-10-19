#!/usr/bin/python3

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, list(input())))
    res = 0
    val = l[0]
    for i in range(1, n):
        if val^l[i]==0:
            res += 1
        val = l[i]
    print(res)
