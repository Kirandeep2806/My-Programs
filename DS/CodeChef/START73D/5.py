for _ in range(int(input())):
	n,y=list(map(int,input().split()))
	arr=list(map(int,input().split()))
	o=0
	for i in arr:
		o|=i
	t=o
	r=y
	p=1
	while t:
		if t&1==1 and r&1==0:
			p=0
			break
		r>>=1
		t>>=1
	else:
		print(o^y)
	if p==0:
		print("-1")
