#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	o=0
	for i in arr:
		if i==1:
			o+=1
	if (n-o)%2==0:
		print("YES")
	else:
		print("NO")

	