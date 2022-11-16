#!/bin/usr/python3

for _ in range(int(input())):
	a,b = list(map(int, input().split()))
	m = a+b
	i=2
	while i*i<=m:
		if m%i==0:break
		i+=1
	else:
		print("Alice")
		continue
	print("Bob")
