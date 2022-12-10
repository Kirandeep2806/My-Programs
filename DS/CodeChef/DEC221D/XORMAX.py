#!/usr/bin/python3

from collections import Counter

for _ in range(int(input())):
	a=input()
	b=Counter(input())
	n=len(a)
	a=Counter(a)
	c=min(a['1'],b['0'])+min(a['0'],b['1'])
	print('1'*c + '0'*(n-c))
