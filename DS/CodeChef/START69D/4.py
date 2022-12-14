#!/usr/bin/python3

from collections import defaultdict

def maxval():
	return 10**5+1

for _ in range(int(input())):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	c=defaultdict(maxval)
	for index,i in enumerate(a):
		c[i]=min(c[i], b[index])
	z=list(c.items())
	# print(z)
	if z.__len__()>=k:
		z.sort(key=lambda x:x[1])
		res=0
		for i in range(k):
			res+=z[i][1]
		print(res)
	else:
		print("-1")
