#!/usr/bin/python3

for i in range(int(input())):
    n,x = list(map(int, input().split()))
    print(x%(n+1))