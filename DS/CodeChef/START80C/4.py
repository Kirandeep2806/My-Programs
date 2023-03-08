#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	s=n*(n+1)//2
	if s%n==0:
		print("-1")
	else:
		l=[]
		cnt=0
		temp=[]
		for i in range(1,n+1):
			cnt+=1
			temp.append(i)
			if cnt==2:
				l+=temp[::-1]
				temp=[]
				cnt=0
		print(*l)
