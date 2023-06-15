from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        vis = [[0 for _ in range(n)] for __ in range(m)]
        res = [[0 for _ in range(n)] for __ in range(m)]
        q = deque()
        oneCount = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j,0))
        dxy = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            x,y,dist = q.popleft()
            for i in range(4):
                dx = x+dxy[i][0]
                dy = y+dxy[i][1]
                if 0<=dx<m and 0<=dy<n and mat[dx][dy]==1 and vis[dx][dy]==0:
                    res[dx][dy] = dist+1
                    vis[dx][dy] = 1
                    q.append((dx,dy,dist+1))
        return res