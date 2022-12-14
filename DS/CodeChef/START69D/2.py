#!/usr/bin/python3

for _ in range(int(input())):
	s=set(map(int,input().split()))
	if len(s)==3:
		print("YES")
	else:
		print("NO")
