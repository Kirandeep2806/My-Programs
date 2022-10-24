#!/usr/bin/python3

arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
	if arr[i]==0:
		arr[i] = -1
# print(arr)

d = {}
prefixSum = 0
maxSubArrayLength = 0

for i in range(n):
	prefixSum += arr[i]
	# print(prefixSum, end=" ")
	if prefixSum == 0:
		maxSubArrayLength = i+1
	if d.get(prefixSum, -1) == -1:
		d[prefixSum] = i
	else:
		maxSubArrayLength = max(maxSubArrayLength, i-d[prefixSum])
# print()
print(maxSubArrayLength)
