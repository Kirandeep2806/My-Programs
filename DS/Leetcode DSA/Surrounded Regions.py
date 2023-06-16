class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        vis = [[0 for _ in range(n)] for __ in range(m)]
        def dfs(i,j):
            nonlocal vis
            vis[i][j] = 1
            if i-1>=0 and board[i-1][j]=="O" and vis[i-1][j]==0:
                dfs(i-1,j)
            if i+1<m and board[i+1][j]=="O" and vis[i+1][j]==0:
                dfs(i+1,j)
            if j-1>=0 and board[i][j-1]=="O" and vis[i][j-1]==0:
                dfs(i,j-1)
            if j+1<n and board[i][j+1]=="O" and vis[i-1][j+1]==0:
                dfs(i,j+1)

        for i in range(n):
            if vis[0][i] == 0 and board[0][i] == "O":
                dfs(0,i)
        for i in range(m):
            if vis[i][0] == 0 and board[i][0] == "O":
                dfs(i,0)
        for i in range(n):
            if vis[m-1][i] == 0 and board[m-1][i] == "O":
                dfs(m-1,i)
        for i in range(m):
            if vis[i][n-1] == 0 and board[i][n-1] == "O":
                dfs(i,n-1)
        for i in range(m):
            for j in range(n):
                if vis[i][j]!=1 and board[i][j]=="O":
                    board[i][j] = "X"
        return board
