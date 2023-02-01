for _ in range(int(input())):
	n,x,y=list(map(int,input().split()))
	if n<=x*y:
		print("YES")
	else:
		print("NO")
