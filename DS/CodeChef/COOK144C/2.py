#!/usr/bin/python3

from collections import Counter
for _ in range(int(input())):
	n=int(input())
	s=input()
	c=Counter(s)
	for i in c:
		if c[i]>1:
			print(n-2)
			break
	else:
		print("-1")