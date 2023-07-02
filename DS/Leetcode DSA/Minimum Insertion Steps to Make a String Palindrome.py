from functools import cache

s = input()
n = len(s)
dp = [[0 for _ in range(n)] for __ in range(n)]

# @cache
# def lps(i,j):
# 	if i==j:
# 		return 1
# 	if i>j:
# 		return 0
# 	if s[i] == s[j]:
# 		return 2 + lps(i+1,j-1)
# 	else:
# 		return max(lps(i+1,j),lps(i,j-1))
# res = lps(0, n-1)
# print(n-res)

for i in range(n-1,-1,-1):
	dp[i][i] = 1
	for j in range(i+1,n):
		if s[i]==s[j]:
			dp[i][j] = 2 + dp[i+1][j-1]
		else:
			dp[i][j] = max(dp[i+1][j], dp[i][j-1])
res = dp[0][n-1]
print(n-res)