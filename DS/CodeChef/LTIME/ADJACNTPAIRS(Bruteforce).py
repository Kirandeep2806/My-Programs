#!/usr/bin/python3

from sys import maxsize

for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = maxsize
    for j in range(q):
        i, x = list(map(int, input().split()))
        arr[i-1] = x
        cloneArr = arr.copy()
        goodness = 0
        isSorted = False
        while isSorted == False:
            temp = 0
            loopBreak = False
            for k in range(1, n):
                temp += 1
                if arr[k] < arr[k-1]:
                    for l in range(k, n):
                        arr[l] += 1
                        loopBreak = True
                        break
                if loopBreak:
                    goodness += 1
                    break
                if temp == n-1:
                    isSorted = True
                    break
        print(goodness)
        arr = cloneArr.copy()
