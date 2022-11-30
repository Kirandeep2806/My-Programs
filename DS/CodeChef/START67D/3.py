#!/usr/bin/python3

from collections import defaultdict

for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	d=defaultdict(int)
	for i in l:
		if i&1:
			d[0]+=1
	if (not d[0]) or (d[0]&1):
		print("NO")
	else:
		print("YES")
	