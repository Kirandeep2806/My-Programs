#!/usr/bin/python3

import sys

def maxSubArraySum(arr,N):
    globalMax = -sys.maxsize-1
    localSum = 0
    startIndex = 0
    endIndex = 0
    for i in range(N):
        localSum += arr[i]
        if localSum > globalMax:
            globalMax = localSum
            endIndex = i
        if localSum < 0:
            localSum = 0
            startIndex = i+1
    return [globalMax, [startIndex, endIndex]]


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    temp = maxSubArraySum(a, n)
    leftSum = sum(a[:temp[1][1]+1])
    rightSum = sum(a[temp[1][0]:])
    if leftSum > rightSum:
        while b!=[]:
            val = b.pop()
            if val > 0:
                leftSum += val
    else:
        while b!=[]:
            val = b.pop()
            if val > 0:
                rightSum += val
    print(max(leftSum, rightSum, temp[0]))
