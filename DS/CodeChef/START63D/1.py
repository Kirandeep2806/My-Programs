#!/usr/bin/python3

for _ in range(int(input())):
	c,ca = list(map(int, input().split()))
	cp = c*2
	cap = ca*5
	if cp>cap:
		print("Chocolate")
	elif cp<cap:
		print("Candy")
	else:
		print("Either")