#!/usr/bin/python3

# from collections import OrderedDict

from logging import getLogRecordFactory


for i in range(int(input())):
    n = int(input())
    strengthOnGround = list(map(int, input().split()))
    strengthOnWater = list(map(int, input().split()))
    strengthOnGround = [i[0] for i in sorted(list(enumerate(strengthOnGround)), key=lambda x:x[1], reverse=True)]
    strengthOnWater = [i[0] for i in sorted(list(enumerate(strengthOnWater)), key=lambda x:x[1], reverse=True)]
    # print(strengthOnGround, strengthOnWater)
    dWater = {}
    dGround = {}
    for index, val in enumerate(strengthOnWater):
        dWater[val] = index
    for index, val in enumerate(strengthOnGround):
        dGround[val] = index
    print(strengthOnGround, strengthOnWater)
    print(dGround, dWater)
    # 0 - consider ground
    # 1 - consider water
    maxVal = 0
    maxCount = 0
    for i in range(n):
        res = 0
        # considerIteration = 0
        # if dGround[strengthOnGround[i]] < dWater[strengthOnWater[i]]:
        #     considerIteration = 1
        # if considerIteration == 1:
        # considerNumbers = n - dGround[strengthOnGround[i]] - 1
        # for j in range(dWater[strengthOnWater[i]], n):
        #     if dGround.get(strengthOnWater[j], -1) != -1:
        #         considerNumbers -= 1
        #     res += 1
        # else:
        considerNumbers = n - dWater[strengthOnWater[i]] - 1
        for j in range(dGround[strengthOnGround[i]]+1, n):
            if dWater.get(strengthOnGround[j], -1) != -1:
                considerNumbers -= 1
            res += 1
        res += considerNumbers
        if res > maxVal:
            maxVal = res
            maxCount = 1
        elif res == maxVal:
            maxCount += 1
    print(maxCount)
