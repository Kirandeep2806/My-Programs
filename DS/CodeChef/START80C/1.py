#!/usr/bin/python3

from math import ceil
for _ in range(int(input())):
	h,x,y=list(map(int,input().split()))
	res=1
	h-=y
	print(res+ceil(h/x))