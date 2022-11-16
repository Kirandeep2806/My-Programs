#!/usr/bin/python3

for _ in range(int(input())):
	a,b = list(map(int, input().split()))
	print("YES" if  a>b else "NO")
