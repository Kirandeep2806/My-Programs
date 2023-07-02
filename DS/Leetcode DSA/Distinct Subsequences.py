# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         @cache
#         def solve(i,j):
#             if j<0:
#                 return 1
#             if i<0:
#                 return 0
#             if s[i] == t[j]:
#                 return solve(i-1, j-1) + solve(i-1, j)
#             else:
#                 return solve(i-1, j)
#         return solve(len(s)-1, len(t)-1)

# Tabulation

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]
