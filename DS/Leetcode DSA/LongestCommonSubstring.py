s = input()
t = input()
n = int(input())
m = int(input())

dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
res = 0

for i in range(1,n+1):
	for j in range(1,m+1):
		if i==0 or j==0:
			dp[i][j] = 0
		if s[i-1] == t[j-1]:
			dp[i][j] = 1+dp[i-1][j-1]
			res = max(res, dp[i][j])
		else:
			dp[i][j] = 0
print(res)