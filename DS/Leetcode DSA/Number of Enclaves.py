class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        dxy = [(0,1),(0,-1),(1,0),(-1,0)]
        vis = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(n):
            if vis[0][i] == 0 and grid[0][i] == 1:
                q.append((0,i))
                vis[0][i] = 1
        for i in range(m):
            if vis[i][0] == 0 and grid[i][0] == 1:
                q.append((i,0))
                vis[i][0] = 1
        for i in range(n):
            if vis[m-1][i] == 0 and grid[m-1][i] == 1:
                q.append((m-1,i))
                vis[m-1][i] = 1
        for i in range(m):
            if vis[i][n-1] == 0 and grid[i][n-1] == 1:
                q.append((i,n-1))
                vis[i][n-1] = 1
        while q:
            x,y = q.popleft()
            for i,j in dxy:
                r,c=x+i,y+j
                if 0<=r<m and 0<=c<n and grid[r][c]==1 and vis[r][c]==0:
                    vis[r][c] = 1
                    q.append((r,c))
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and vis[i][j]==0:
                    res += 1
        return res