#!/usr/bin/python3

for _ in range(int(input())):
	a,b,x,y = list(map(int, input().split()))
	if (a>=b and (a-b)<=y) or (a<=b and (b-a)<=x):
		print("YES")
	else:
		print("NO")
