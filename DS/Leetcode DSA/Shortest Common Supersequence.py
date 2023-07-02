s = input()
t = input()

m = len(s)
n = len(t)

dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

for i in range(1,m+1):
	for j in range(1,n+1):
		if i==0 or j==0:
			dp[i][j] = 0
		if s[i-1] == t[j-1]:
			dp[i][j] = 1+dp[i-1][j-1]
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i = m
j = n

res = ""

while i>0 and j>0:
	if s[i-1] == t[j-1]:
		res += s[i-1]
		i -= 1
		j -= 1
	elif dp[i-1][j] > dp[i][j-1]:
		res += s[i-1]
		i -= 1
	else:
		res += t[j-1]
		j -= 1

while i>0:
	res += s[i-1]
	i -= 1

while j>0:
	res += t[j-1]
	j -= 1

print(res[::-1])