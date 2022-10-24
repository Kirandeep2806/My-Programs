#!/usr/bin/python3

from sys import maxsize

arr = list(map(int, input().split()))
n = arr.__len__()
target = int(input())
d = {}
maxVal = -maxsize

sumTillNow = 0
for i in range(n):
	sumTillNow += arr[i]
	valueToCheck = sumTillNow - target
	if valueToCheck==0:
		maxVal = i+1
	if d.get(sumTillNow, -1)==-1:
		d[sumTillNow] = i
	if d.get(valueToCheck, -1)!=-1:
		maxVal = max(maxVal, i-d[valueToCheck])

print("Longest Subarray with the given sum : ", maxVal)
