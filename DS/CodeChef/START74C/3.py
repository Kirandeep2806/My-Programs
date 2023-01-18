#!/usr/bin/python3

def gcd(a,b):
	if b==0:
		return a
	return gcd(b, a%b)

for _ in range(int(input())):
	a,b=list(map(int,input().split()))
	if b%a==0:
		print(0)
	else:
		x,y=a,b
		if a<b:
			a,b=b,a
		n=gcd(a,b)
		r=(x*n)//n
		print(r-gcd(y,n))
