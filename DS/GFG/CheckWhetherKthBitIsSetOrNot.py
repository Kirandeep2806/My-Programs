#!/usr/bin/python3

n = int(input())
k = int(input())

if (n>>k)&1==1:
    print("Yes")
else:
    print("No")
