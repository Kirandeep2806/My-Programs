from collections import Counter
for _ in range(int(input())):
	n=int(input())
	t=input()
	l=Counter(t)
	if l['1']>l['0']:
		print(1+l['0'])
	else:
		print(l['1'])