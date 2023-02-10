from typing import List

class Solution:
    def compute(self,x,y,n,grid,memset,cnt):
        if grid[x][y]==1 or (abs(x-y)==n):
            # print(x,y,cnt)
            return cnt
        # if grid[x][y]!=float("inf"):
        #     return grid[x][y]
        if x>0:
            t=self.compute(x-1,y,n, grid, memset,cnt+1)
            print(t)
            memset[x][y]=min(memset[x][y],t) #top
        if y<n-1:
            r=self.compute(x,y+1,n, grid, memset,cnt+1)
            memset[x][y]=min(memset[x][y],r) #right
        if x<n-1:
            b=self.compute(x+1,y,n, grid, memset,cnt+1)
            memset[x][y]=min(memset[x][y],b) #bottom
        if y>0:
            l=self.compute(x,y-1,n, grid, memset,cnt+1)
            memset[x][y]=min(memset[x][y],l) #left
        return memset[x][y]


    def maxDistance(self, grid) -> int:
        n=len(grid)
        memset=[[float("inf")]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                memset[i][j]=self.compute(i,j,n,grid,memset,0)
        print(memset)

s=Solution().maxDistance(eval(input()))
print(s)
