s = input()
t = s[::-1]
m = len(s)
dp = [[0 for _ in range(m+1)] for __ in range(m+1)]
for i in range(1,m+1):
	for j in range(1,m+1):
		if i==0 or j==0:
			dp[i][j] = 0
		if s[i-1] == t[j-1]:
			dp[i][j] = 1+dp[i-1][j-1]
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[m][m])