from collections import defaultdict

for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	s=[]
	temp=[]
	for i in range(n):
		temp.append((i,a[i]))
		s.append((i,a[i]+b[i]))
	s.sort(key=lambda x:x[1])
	temp.sort(key=lambda x:x[1])
	# print(temp)
	# print(s)
	i=0
	d=defaultdict(bool)
	res=0
	while i<n and k-s[i][1]>=0:
		res+=1
		k-=s[i][1]
		d[s[i][0]]=True
		i+=1

	if i<n:
		for j in range(n):
			if d[temp[j][0]]==False:
				k-=temp[j][1]
				if k>=0:
					res+=1
					break
	print(res)
