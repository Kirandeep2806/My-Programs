#!/usr/bin/python3

l = [1, 8, 30, -5, 20, 7]
k = 4

curSum = sum(l[:k])
maxSum = curSum

for i in range(k, len(l)):
    curSum -= l[i-k]
    curSum += l[i]
    maxSum = max(maxSum, curSum)

print(maxSum)
