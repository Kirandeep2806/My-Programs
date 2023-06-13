#!/usr/bin/python3

for _ in range(int(input())):
    x,y = list(map(int, input().split()))
    y = 2*y
    if 15*x<=y:
        print("YES")
    else:
        print("NO")
