for _ in range(int(input())):
	n=int(input())
	if n==0:
		print(1,3,4,5)
		continue
	c=n+2
	d=c^n
	a=2
	while True:
		b=a-1
		if a!=d and b!=d and a!=c and b!=c and a!=b:
			break
		a<<=1
	print(a,b,c,d)
