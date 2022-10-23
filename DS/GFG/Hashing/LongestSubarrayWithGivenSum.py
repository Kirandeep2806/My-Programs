#!/usr/bin/python3

from collections import defaultdict

def defaultVal():
	return -1

arr = list(map(int, input().split()))
n = arr.__len__()
target = int(input())
d = defaultdict(defaultVal)

prefixSum = [arr[0]]
d[prefixSum[0]] = 0
for i in range(1, n):
	prefixSum.append(arr[i] + prefixSum[i-1])
	if d[prefixSum[i]]==-1:
		d[prefixSum[i]] = i

print(prefixSum, d)
