from math import ceil
for _ in range(int(input())):
	x,y,z = list(map(int, input().split()))
	print(x*ceil(y/z))