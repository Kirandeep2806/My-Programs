#!/usr/bin/python3

from collections import defaultdict

mod=10**9+7
for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	d=defaultdict(int)
	res=0
	for i in l:
		d[i]+=1
	pre=1
	for i in range(1,n+1):
		t=(pre*d[i])%mod
		res=(res+t)%mod
		pre=t
	print(res)

