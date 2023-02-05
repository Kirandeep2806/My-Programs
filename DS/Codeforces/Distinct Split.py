#!/usr/bin/python3

for _ in range(int(input())):
	n=int(input())
	s=input()

	arr1=[0]*n
	arr2=[0]*n

	a1s=set()
	a2s=set()

	a1s.add(s[0])
	a2s.add(s[n-1])

	arr1[0]=1
	arr2[n-1]=1

	for i in range(1,n):
		if s[i] in a1s:
			arr1[i]=arr1[i-1]
		else:
			arr1[i]=arr1[i-1]+1
			a1s.add(s[i])

		if s[n-i-1] in a2s:
			arr2[n-i-1]=arr2[n-i]
		else:
			arr2[n-i-1]=arr2[n-i]+1
			a2s.add(s[n-i-1])
	res=0
	for i in range(1,n):
		res=max(res,arr1[i-1]+arr2[i])
		if i!=n-1:
			res=max(res, arr1[i]+arr2[i+1])
	print(res)
