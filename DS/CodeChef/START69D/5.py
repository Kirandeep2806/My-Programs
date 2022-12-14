#!/usr/bin/python3

from collections import Counter

for _ in range(int(input())):
	n=int(input())
	l=input()
	c=Counter(l)
	s=set([i+1 for i in range(n)])
	if c.__len__()==1:
		print("-1")
	else:
		res=[]
		temp=n
		for i,v in enumerate(l):
			if v=='1':
				s.discard(i+1)
				res.append(i+1)
				temp-=1
				if temp==0:
					break
		if temp>0:
			for i in s:
				res.append(i)
				temp-=1
				if temp==0:
					break
		res.sort()
		print(*res)
