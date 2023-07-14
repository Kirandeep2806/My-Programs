#User function Template for python3

from collections import deque

class Solution:
    def shortestDistance(self,n,m,grid,X,Y):
        if X==Y==0:
            if grid[0][0]:
                return 0
            return -1
        if grid[X][Y] == 0:
            return -1
        q = deque([(0,0,1)])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        while q:
            x,y,steps = q.popleft()
            for i in range(4):
                newx = x+dr[i]
                newy = y+dc[i]
                if newx == X and newy == Y:
                    return steps
                if 0<=newx<n and 0<=newy<m and grid[newx][newy]==1:
                    grid[newx][newy] = 0
                    q.append((newx,newy,steps+1))
        return -1
