#!/usr/bin/python3

arr = list(map(int, input().split()))
targetSum = int(input())

ptr = 0
n = len(arr)
currSum = 0
windowSize = 0
found = False

while ptr<=n:
    if currSum < targetSum:
        if ptr >= n:
            break
        currSum += arr[ptr]
        windowSize += 1
        ptr += 1
    elif currSum > targetSum:
        currSum -= arr[ptr-windowSize]
        windowSize -= 1
    else:
        found = True
        break

if found:
    print("Yes :", windowSize)
else:
    print("No")
