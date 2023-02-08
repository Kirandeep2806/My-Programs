#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	l=[i for i in range(1,n+1)]
	print(*(l[1:]+l[:1]))
