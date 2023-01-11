for _ in range(int(input())):
	x,y=list(map(int,input().split()))
	if x*3<=y:
		print("YES")
	else:
		print("NO")