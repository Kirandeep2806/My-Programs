#!/usr/bin/python3

for i in range(int(input())):
    a,b,x,y = list(map(int, input().split()))
    alice = a/x
    bob = b/y
    if bob > alice:
        print("BOB")
    elif bob < alice:
        print("ALICE")
    else:
        print("EQUAL")
