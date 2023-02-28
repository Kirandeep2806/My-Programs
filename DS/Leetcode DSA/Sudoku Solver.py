class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(row,col,val):
            for i in range(9):
                if board[i][col]==val:
                    return False
                if board[row][i]==val:
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3]==val:
                    return False
            return True

        def solve():
            nonlocal board
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in range(1,10):
                            k=str(k)
                            if isValid(i,j,k):
                                board[i][j]=k
                                if solve():
                                    return True
                            board[i][j]='.'
                        return False
            return True
        solve()
