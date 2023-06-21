for _ in range(int(input())):
	n,m,h = list(map(int, input().split()))
	ec = list(map(int, input().split()))
	p = list(map(int, input().split()))
	ec.sort(reverse=True)
	p.sort(reverse=True)
	res = 0
	for i in range(min(n,m)):
		if p[i]*h >= ec[i]:
			res += ec[i]
		else:
			res += p[i]*h
	print(res)
