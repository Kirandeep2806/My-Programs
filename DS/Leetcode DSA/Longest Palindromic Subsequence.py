s = input()
m = len(s)
dp = [[0 for _ in range(m+1)] for __ in range(m+1)]

# Striver Approach

# t = s[::-1]
# for i in range(1,m+1):
# 	for j in range(1,m+1):
# 		if i==0 or j==0:
# 			dp[i][j] = 0
# 		if s[i-1] == t[j-1]:
# 			dp[i][j] = 1+dp[i-1][j-1]
# 		else:
# 			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print(dp[m][m])

# Another Approach

from functools import cache

@cache
def solve(i,j):
	if i==j:
		return 1
	if i>j:
		return 0
	if s[i] == s[j]:
		return 2 + solve(i+1,j-1)
	else:
		return max(solve(i+1,j),solve(i,j-1))
res = solve(0, m-1)
print(res)


# Tabulation

# for i in range(n-1,-1,-1):
# 	for j in range(i+1,n):
# 		if i==j:
# 			dp[i][j] = 1
# 		elif s[i]==s[j]:ab
# 			dp[i][j] = 2 + dp[i+1][j-1]
# 		else:
# 			dp[i][j] = max(dp[i+1][j], dp[i][j-1])
# print(dp[0][n-1])
