from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        time=0
        visited=[]
        oneCount=0
        res=0
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append(0)
                if grid[i][j]==1:
                    oneCount+=1
                if grid[i][j]==2:
                    q.append((i,j))
            visited.append(temp)

        while q:
            temp=deque()
            time+=1
            for i in range(len(q)):
                v=q.popleft()
                drow=[0,0,1,-1]
                dcol=[-1,1,0,0]
                for i in range(4):
                    r1=v[0]+drow[i]
                    c1=v[1]+dcol[i]
                    if 0<=r1<m and 0<=c1<n and grid[r1][c1]==1 and visited[r1][c1]==0:
                        oneCount-=1
                        temp.append((r1,c1))
                        visited[r1][c1]=1
            q=temp.copy()

        if oneCount!=0:
            return -1
        elif time!=0:
            return time-1
        return 0

s=Solution().orangesRotting(eval(input()))
print(s)
