#!/usr/bin/python3

for _ in range(int(input())):
    n = int(input())
    res = 0
    if n==1 or n==2:
        print(0)
    elif n==3:
        print(2)
    elif n==4:
        print(3)
    elif n==5:
        print(5)
    else:
        t = n-4
        even = t//2
        odd = t-even
        res += even + 2*odd + 3
        print(res)
