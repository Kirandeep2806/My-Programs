#!/bin/usr/python3

from collections import defaultdict
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	d = defaultdict(int)
	for i in arr:
		d[i] += 1
		if d[i]==3:
			break
	else:
		print("Yes")
		continue
	print("No")
