for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	so = []
	sa = []
	t1 = []
	t2 = []

	for i in range(n):
		if a[i]!=0:
			t1.append(a[i])
		else:
			so.append(t1)
			t1 = []
		if b[i]!=0:
			t2.append(b[i])
		else:
			sa.append(t2)
			t2 = []
	else:
		if t1:
			so.append(t1)
		if t2:
			sa.append(t2)
	mo = ma = 0
	for i in so:
		mo = max(mo, len(i))
	for i in sa:
		ma = max(ma, len(i))
	if mo > ma:
		print("Om")
	elif ma > mo:
		print("Addy")
	else:
		print("Draw")

