#!/usr/bin/python3

from math import log10, ceil

for i in range(int(input())):
    numInt = int(input())
    num = str(numInt)
    if numInt%9 == 0:
        num = num[0] + "0" + num[1:]
        print(f"Case #{i+1}: {num}")
    else:
        num = str(numInt)
        numberSum = 0
        count = 0
        bound = int(log10(numInt)) + 1
        while count < bound:
            numberSum += numInt % 10
            numInt //= 10
            count += 1
        diff = ceil(numberSum/9)*9 - numberSum
        count = 0
        isSet = False
        while count < bound:
            if diff >= int(num[count]):
                count += 1
            else:
                num = num[:count] + str(diff) + num[count:]
                isSet = True
                break
        if isSet:
            print(f"Case #{i+1}: {int(num)}")
        else:
            print(f"Case #{i+1}: {num + str(diff)}")
