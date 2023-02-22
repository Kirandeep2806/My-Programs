for _ in range(int(input())):
	n,x=list(map(int,input().split()))
	arr=list(map(int,input().split()))
	arr.sort()
	print(arr[n-x]-1)
	