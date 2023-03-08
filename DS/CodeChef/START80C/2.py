#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	res=0
	for i in range(n):
		if a[i]==b[i]:res+=1
		elif a[i]<b[i]:
			if b[i]<=2*a[i]:
				res+=1
		else:
			if a[i]<=2*b[i]:
				res+=1
	print(res)
