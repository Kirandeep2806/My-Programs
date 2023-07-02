from functools import lru_cache

class Solution:
    def minDistance(self, s: str, t: str) -> int:
        # @lru_cache(None)
        # def solve(i,j):
        #     if i<0:
        #         return j+1
        #     if j<0:
        #         return i+1
        #     if s[i] == t[j]:
        #         return solve(i-1,j-1)
        #     else:
        #         insert = solve(i,j-1)
        #         delete = solve(i-1,j)
        #         replace = solve(i-1,j-1)
        #         return min(insert, delete, replace)+1
        # return solve(len(s)-1, len(t)-1)

        # Tabulation

        m = len(s)
        n = len(t)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[m][n]
