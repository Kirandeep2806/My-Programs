def countZeroes(num):
	res=0
	while num>0:
		num=num&(num-1)
		res+=1
	return res

for _ in range(int(input())):
	n=int(input())
	num=int(input(),base=2)
	res1=countZeroes(num)
	if num==1 or num==2:
		print("NO")
	elif res1<=3:
		print("YES")
	else:
		print("NO")