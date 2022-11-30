#!/usr/bin/python3

for _ in range(int(input())):
	n,x1,y1,x2,y2=list(map(int,input().split()))
	print(min(abs(x1-x2)+abs(y1-y2),min(min(x1,n+1-x1),min(y1,n+1-y1))+min(min(x2,n+1-x2),min(y2,n+1-y2))))
