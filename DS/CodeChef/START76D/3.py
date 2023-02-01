for _ in range(int(input())):
	l=list(map(int,input().split()))
	n=len(l)
	if sum(l)>=(n*(n+1))//2:
		print("YES")
	else:
		print("NO")