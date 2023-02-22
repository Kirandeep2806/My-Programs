for _ in range(int(input())):
	x,y=list(map(int,input().split()))
	if y>x:
		print(x+(y-x)*2)
	else:
		print(y)
	