#!/usr/bin/python3

for _ in range(int(input())):
    m,n,p = list(map(int, input().split()))
    l = [0]*n
    allWalks = []
    for i in range(m):
        dayWalks = list(map(int, input().split()))
        allWalks.append(dayWalks)
        for j in range(n):
            l[j] = max(dayWalks[j], l[j])
    res = 0
    for i in range(n):
        res += l[i] - allWalks[p-1][i]
    print(f"Case #{_+1}: {res}")
