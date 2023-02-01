from math import ceil
for _ in range(int(input())):
	n,x=list(map(int,input().split()))
	a=list(map(int,input().split()))
	even=0
	for i in a:
		if i&1==0:
			even+=1
	if x&1:
		print(ceil(even/2))
	elif even!=n:
		print(even)
	else:
		print("-1")
