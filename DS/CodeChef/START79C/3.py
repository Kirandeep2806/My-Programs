#!/usr/bin/python3
from math import ceil
def fpf(n):
	i=2
	while i*i<=n:
		while n%i==0:
			return i
		i+=1
	if n>1:
		return n

for _ in range(int(input())):
	x,y=list(map(int,input().split()))
	temp=x
	cnt=0
	while x%2!=0:
		cnt+=1
		x+=fpf(x)
	cnt+=ceil((y-x)/2)
	print(cnt)
