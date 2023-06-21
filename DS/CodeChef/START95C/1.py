for _ in range(int(input())):
	n = int(input())
	l = input().split(" ")
	# a,b,ab,o
	arr = [0]*4
	for i in range(n):
		if l[i] == "A":
			arr[0] += 1
		elif l[i] == "B":
			arr[1] += 1
		elif l[i] == "AB":
			arr[2] += 1
		else:
			arr[3] += 1
	res = 0
	if arr[0]:
		res = max(res, arr[0] + arr[2])
	if arr[1]:
		res = max(res, arr[1] + arr[2])
	if arr[2]:
		res = max(res, arr[2])
	if arr[3]:
		res = max(res, arr[3] + res)
	print(res)