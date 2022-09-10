#!/usr/bin/python3

for i in range(int(input())):
    w,x,y,z = list(map(int, input().split()))
    print(w+(x-y)*z)

