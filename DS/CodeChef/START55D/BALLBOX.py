#!/usr/bin/python3

for i in range(int(input())):
    n, k = list(map(int, input().split()))
    if n >= ((k*(k+1))//2):
        print("YES")
    else:
        print("NO")
