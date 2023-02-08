#!/usr/bin/python3

for _ in range(int(input())):
	a,b,c,x=list(map(int,input().split()))
	s={a+b,b+c,a+c}
	for i in s:
		if i>=x:
			print("YES")
			break
	else:
		print("NO")
	