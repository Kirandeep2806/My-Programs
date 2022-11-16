#!/bin/usr/python3

for _ in range(int(input())):
	n,k = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	for index, i in enumerate(arr):
		if index!=n-1 and i==k:
			print("Yes")
			break
	else:
		if n==1 and k==arr[0]:
			print("Yes")
		else:
			print('No')
