#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    l = list(input())
    res = ''
    chance = 0

    while l!=[]:
        if chance%2 == 0:
            temp = l.pop(0)
            if temp == '0':
                res = temp + res
            else:
                res = res + temp
        else:
            temp = l.pop()
            if temp == '0':
                res = res + temp
            else:
                res = temp+res
        chance += 1
    print(res)
