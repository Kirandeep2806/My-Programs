from collections import defaultdict

for _ in range(int(input())):
	d=defaultdict(bool)
	n,k=list(map(int,input().split()))
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	temp=sorted(enumerate(a),key=lambda x:x[1])
	res=0

	s=[]
	for i in range(n):
		s.append((i,a[i]+b[i]))

	s.sort(key=lambda x:x[1])
	i=0
	while i<n and k>=0:
		res+=1
		k-=s[i][1]
		d[s[i][0]]=True
		i+=1

	# print(s,k,res)
	# print(temp)
	if k<0:
		k+=b[s[i-1][0]]
		if k<0:
			k+=a[s[i-1][0]]
			del d[s[i-1][0]]
			# print(k,temp,d)
			for i,val in temp:
				if not d[i]:
					k-=val
					# print(val)
					break
			if k<0:
				res-=1

	print(res)
