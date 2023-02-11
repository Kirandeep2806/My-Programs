from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        q=deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    q.append([i,j])

        res=-float("inf")
        coordinates=[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            x,y=q.popleft()
            for i,j in coordinates:
                x_temp,y_temp=x+i,y+j
                if 0<=x_temp<n and 0<=y_temp<n and grid[x_temp][y_temp]==0:
                    grid[x_temp][y_temp]=grid[x][y]+1
                    res=max(res, grid[x_temp][y_temp])
                    q.append([x_temp,y_temp])
        return res-1

s=Solution().maxDistance(eval(input()))
print(s)
