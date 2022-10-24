#!/usr/bin/python3

from itertools import accumulate
import operator

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
n = len(arr1)

arr3 = []

for i in range(n):
	arr3.append(arr1[i] - arr2[i])

# Find the longest subarray with 0 sum for arr3

d = {}
prefixSum = 0
maxSubArrayLength = 0

for i in range(n):
	prefixSum += arr3[i]
	if prefixSum == 0:
		maxSubArrayLength = i+1
	if d.get(prefixSum, -1) == -1:
		d[prefixSum] = i
	else:
		maxSubArrayLength = max(maxSubArrayLength, i-d[prefixSum])

print(maxSubArrayLength)
