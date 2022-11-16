#!/usr/bin/python3

from collections import Counter

for _ in range(int(input())):
	n = int(input())
	c = Counter(input())
	for i in c:
		if c[i]&1:
			print("NO")
			break
	else:
		print("YES")
