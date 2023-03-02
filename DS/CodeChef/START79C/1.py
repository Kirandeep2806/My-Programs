#!/usr/bin/python3
from math import ceil
for _ in range(int(input())):
	arr=list(map(int,input().split()))
	f=ceil(100-(100*(arr[0]/100)))
	s=ceil(200-(200*(arr[1]/100)))
	if f>s:
		print("SECOND")
	elif s>f:
		print("FIRST")
	else:
		print("BOTH")