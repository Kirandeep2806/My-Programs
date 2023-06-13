#!/usr/bin/python3

for _ in range(int(input())):
    n = int(input())
    res = 0
    l = list(map(int, input().split()))
    score = 0
    for i in range(n):
        score += l[i]
        sr = score*100/(i+1)
        if sr == 100:
            res += 1
    print(res)