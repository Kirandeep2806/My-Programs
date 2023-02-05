#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	s=input()
	for i in range(n//2):
		if s[i]==s[n-i-1]:
			print(n-i*2)
			break
	else:
		if n&1:
			print("1")
		else:
			print("0")


