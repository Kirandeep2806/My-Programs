#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	l=[i for i in range(1,n+1)]
	res=l[:n//2][::-1]+l[n//2:]
	print(*res)
