#!/usr/bin/python3

s=input()
n=len(s)
d={}
num=1
for i in sorted(s):
	d[i]=num
	num+=1
print(d)
res=0

mul=n-1
print(mul)
for i in range(mul,-1,-1):
	res+=(d[i]*mul)

print(res)
