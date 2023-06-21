from collections import defaultdict
from math import log2
for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	l.sort()
	arr = []
	hm = defaultdict(int)
	for i in range(n):
		temp = int(log2(l[i]))+1
		hm[temp] += 1
		arr.append(temp)
	arr.sort()
	length = len(arr)
	print((hm[arr[-1]] + 1)//2)