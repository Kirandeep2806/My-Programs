#!/usr/bin/python3

for i in range(int(input())):
    l = list(map(int, input().split()))
    even = False
    odd = False
    for j in l:
        if even and odd:
            print("YES")
            break
        if j&1:
            odd = True
        else:
            even = True
    else:
        if even and odd:
            print("YES")
        else:
            print("NO")
