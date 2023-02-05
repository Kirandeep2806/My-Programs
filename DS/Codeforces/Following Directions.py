#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	moves=input()
	x=y=0
	for i in range(n):
		if moves[i]=="U":
			y+=1
		elif moves[i]=="D":
			y-=1
		elif moves[i]=="L":
			x-=1
		else:
			x+=1
		if x==1 and y==1:
			print("YES")
			break
	else:
		print("NO")
