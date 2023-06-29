from sys import setrecursionlimit
setrecursionlimit(10000)
class Solution:
    def cutRod(self, n, prices):
        l = len(prices)
        dp = [[-1 for _ in range(n+1)] for __ in range(l)]
        def solve(i,n):
            if i == 0:
                return n*prices[0]
            if dp[i][n] != -1:
                return dp[i][n]
            notPick = solve(i-1, n)
            pick = 0
            if i+1 <= n:
                pick = prices[i] + solve(i, n-i-1)
            dp[i][n] = max(pick, notPick)
            return dp[i][n]
        return solve(l-1, n)

s = Solution()
res = s.cutRod(int(input()), list(map(int, input().split())))
print(res)
