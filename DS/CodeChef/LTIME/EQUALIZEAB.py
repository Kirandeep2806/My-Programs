#!/usr/bin/python3

for i in range(int(input())):
    a,b,x = list(map(int, input().split()))
    # diff = abs(a-b)
    # if ((a&1 and b&1) or (a&1==0 and b&1==0)) and (x<diff):
    #     print("YES")
    # else:
    #     print("NO")
    diff = abs(a-b)
    if a == b:
        print("YES")
    elif diff%2 == 0:
        diffFromCenter = abs(((a+b)//2) - a)
        if (x<=diff//2) and (diffFromCenter%x == 0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
