#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    strengthOnGround = list(map(int, input().split()))
    strengthOnWater = list(map(int, input().split()))
    # sortedGround = sorted(list(enumerate(strengthOnGround)), key=lambda x:x[1], reverse=True)
    # sortedWater = sorted(list(enumerate(strengthOnWater)), key=lambda x:x[1], reverse=True)
    l1 = set()
    l2 = set()
    lg = [0]*n
    lw = lg.copy()
    res = 0
    maxStrength = 0
    for i in range(n):
        pass
        # lg[sortedGround[i][0]] += n-i-1
        # maxStrength = max(maxStrength, lg[sortedGround[i][0]])
    # print(sortedGround)
    # print(lg)
    for i in range(n):
        pass
        # lw[sortedWater[i][0]] += n-i-1
    # print(sortedWater)
    print(lg)
