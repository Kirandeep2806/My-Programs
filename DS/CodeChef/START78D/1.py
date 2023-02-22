for _ in range(int(input())):
	l=list(map(int,input().split()))
	if l[0]+l[1]>6:
		print("YES")
	else:
		print("NO")