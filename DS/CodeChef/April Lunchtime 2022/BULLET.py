#!/usr/bin/python3

for _ in range(int(input())):
    x,y,z = list(map(int, input().split()))
    if y//x < z:
        print(z-y//x)
    else:
        print(0)

