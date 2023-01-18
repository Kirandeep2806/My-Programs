#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	s=float("inf")
	neg=-float("inf")
	ns=False
	ss=False
	end=False
	isOne=False
	for i in arr:
		if i==0:
			end=True
			break
		if i>0:
			s=min(i, s)
			ss=True
		elif i<0:
			neg=max(neg, i)
			ns=True
	if end:
		print("-1")
	elif s==1 or neg==-1:
		print("0")
	elif ns and ss:
		print(min(s,abs(neg))-1)
	elif ns:
		print(abs(neg)-1)
	elif ss:
		print(s-1)
	else:
		print("-1")
