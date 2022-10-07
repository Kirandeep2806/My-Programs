#!/usr/bin/python3

for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    t1 = a/b
    t2 = c/d
    if t1 == t2:
        print("Both")
    elif t1>t2:
        print("Chefina")
    else:
        print("Chef")
