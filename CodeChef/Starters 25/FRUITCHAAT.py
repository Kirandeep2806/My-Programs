#!/usr/bin/python3

for i in range(int(input())):
    x,y = list(map(int, input().split()))
    print(x//2 if x//2<y else y)