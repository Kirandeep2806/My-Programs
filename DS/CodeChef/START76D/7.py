for _ in range(int(input())):
	n=int(input())
	if n&1:
		print("-1")
		continue
	l=[0]*n
	num=0
	for i in range(n//2):
		if i&1==0:
			l[i]=num
			num+=1
			l[n-i-1]=-num
		else:
			l[i]=-num
			num=abs(num)+1
			l[n-i-1]=num
	print(*l)
