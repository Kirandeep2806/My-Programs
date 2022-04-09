#!/usr/bin/python3

for i in range(int(input())):
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l3 = list(map(int, input().split()))
    minList = [min(l1[i], l2[i], l3[i]) for i in range(4)]
    maxValue = 1000000
    if sum(minList) >= maxValue:
        res = []
        loopCounter = 0
        sumCounter = 0
        for j in minList:
            if sumCounter < maxValue:
                if j <= maxValue-sumCounter:
                    res.append(j)
                    sumCounter += j
                    loopCounter += 1
                else:
                    res.append(maxValue-sumCounter)
                    sumCounter = maxValue
                    loopCounter += 1
                    break
            else:
                break
        if loopCounter < 4:
            for k in range(loopCounter, 4):
                res.append(0)

        print("Case #{}: ".format(i+1), end="")
        print(*res)
    else:
        print("Case #{}: {}".format(i+1, "IMPOSSIBLE"))
