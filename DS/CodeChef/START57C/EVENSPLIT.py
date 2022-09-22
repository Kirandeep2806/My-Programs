#!/usr/bin/python3

for i in range(int(input())):
    a,b = list(map(int, input().split()))
    if (a&1 and b&1) or (a == 1 or b == 1):
        print("No")
    else:
        print("Yes")
