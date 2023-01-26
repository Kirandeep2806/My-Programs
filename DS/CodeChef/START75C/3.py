for _ in range(int(input())):
	n=int(input())
	l=input()
	arr=[]
	onesCount=0
	for i in range(n-1,-1,-1):
		if l[i]=='1':
			onesCount+=1
		else:
			if onesCount:
				arr.append(onesCount)
			onesCount=0
	if onesCount:
		arr.append(onesCount)
	arr=arr[::-1]
	if arr==[]:
		print("0")
	elif l[0]=='0':
		print(max(arr))
	else:
		if len(arr)>1:
			temp=arr.pop(0)
			print(temp+max(arr))
		else:
			print(max(arr))