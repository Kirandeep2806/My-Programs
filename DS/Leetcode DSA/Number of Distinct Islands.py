from typing import List

grid = [[1,0,1,0],[0,1,0,1],[0,0,0,1]]
m = len(grid)
n = len(grid[0])
vis = [[0 for _ in range(n)] for __ in range(m)]

hm = set()

def dfs(i,j,prev,l):
    vis[i][j]=1
    l.append((prev[0]-i,prev[1]-j))
    if i-1>=0 and vis[i-1][j]==0 and grid[i-1][j]==1:dfs(i-1,j,(i,j),l)
    if i+1<m and vis[i+1][j]==0 and grid[i+1][j]==1:dfs(i+1,j,(i,j),l)
    if j-1>=0 and vis[i][j-1]==0 and grid[i][j-1]==1:dfs(i,j-1,(i,j),l)
    if j+1<n and vis[i][j+1]==0 and grid[i][j+1]==1:dfs(i,j+1,(i,j),l)

for i in range(m):
    for j in range(n):
        if vis[i][j]==0 and grid[i][j]==1:
            l = []
            dfs(i,j,(i,j),l)
            hm.add(tuple(l))

print(hm)
