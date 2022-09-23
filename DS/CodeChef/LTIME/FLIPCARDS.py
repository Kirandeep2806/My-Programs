#!/usr/bin/python3

for i in range(int(input())):
    a,b = list(map(int, input().split()))
    print(min(b, a-b))
