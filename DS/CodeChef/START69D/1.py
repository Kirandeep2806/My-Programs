#!/usr/bin/python3

for _ in range(int(input())):
	n = int(input())
	if n<3:
		print("LIGHT")
	elif n>=3 and n<7:
		print("MODERATE")
	else:
		print("HEAVY")

