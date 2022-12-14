#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort()
	res=0
	for index,i in enumerate(l):
		val=(index+1-i)
		if val<0:
			print("-1")
			break
		res += (index+1-i)
	else:
		print(res)
