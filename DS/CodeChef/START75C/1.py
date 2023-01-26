for _ in range(int(input())):
	a,b,c,d=list(map(int,input().split()))
	s=set([i for i in range(a,b+1)])
	p=set([i for i in range(c,d+1)])
	print(len(s|p))
