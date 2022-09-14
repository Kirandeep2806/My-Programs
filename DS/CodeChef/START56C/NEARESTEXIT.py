#!/usr/bin/python3

t = int(input())
while t > 0:
    n = int(input())
    if 1<=n<=50:
        print("LEFT")
    else:
        print("RIGHT")
    t -= 1

