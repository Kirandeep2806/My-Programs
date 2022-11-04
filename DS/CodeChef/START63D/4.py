#!/usr/bin/python3

from collections import Counter
from sys import maxsize

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	m = -maxsize
	c = Counter(arr)
	for i in c:
		m = max(m, c[i]+c.get(i^1, 0))
	print(n-m)
