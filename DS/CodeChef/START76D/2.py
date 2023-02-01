for _ in range(int(input())):
	l=list(map(int,input().split()))
	d=["ALICE","BOB","CHARLIE"]
	print(d[l.index(min(l))])