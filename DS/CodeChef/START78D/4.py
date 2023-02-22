for _ in range(int(input())):
	n,x=list(map(int,input().split()))
	if x<(-n+1) or x>(n+1):
		print("-1")
	else:
		cnt=0
		expr=1
		res=""
		if x<=0:
			while expr!=x:
				res+="-"
				expr-=1
				cnt+=1
		else:
			while expr!=x:
				res+="+"
				expr+=1
				cnt+=1
		res+="*"*(n-cnt)
		print(res)
