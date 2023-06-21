n = int(input())
l = []
for _ in range(n):
	l.append(input())
s = set()
res = ""
for i in range(n-1, -1, -1):
	if l[i] not in s:
		s.add(l[i])
		res += l[i][-2:]
print(res)