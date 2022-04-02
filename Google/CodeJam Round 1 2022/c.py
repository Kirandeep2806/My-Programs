#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    dices = list(map(int, input().split()))
    if n == 1:
        print("Case #{}: {}".format(i+1, n))
    else:
        res = 0
        index = 0
        dices.sort()
        for side in dices:
            if index+1 <= side:
                res += 1
                index += 1
        print("Case #{}: {}".format(i+1, res))

