class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        # Memoization

        '''dp = [[-1 for _ in range(n)] for __ in range(m)]
        def solve(i,j):
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return 20001
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j] = min(solve(i,j-1),solve(i-1,j)) + grid[i][j]
            return dp[i][j]
        return solve(m-1,n-1)'''

        # Tabulation

        dp = [[0 for _ in range(n)] for __ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i!=0 or j!=0:
                    left = 20001
                    right = 20001
                    if i>0:
                        left = dp[i-1][j]
                    if j>0:
                        right = dp[i][j-1]
                    dp[i][j] = min(left, right) + grid[i][j]
        return dp[m-1][n-1]
