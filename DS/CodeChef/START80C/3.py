#!/usr/bin/python3
from collections import Counter
for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	c=Counter(l)
	t=[]
	for i,j in c.items():
		t.append((i,j))
	t.sort(key=lambda x:x[1],reverse=True)
	print(n-t[0][1])
	