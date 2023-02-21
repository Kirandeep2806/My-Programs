from typing import List

class Solution:
    def isSafe(self,n,row,col,arr):
        for i in range(row):
            if arr[i][col]=="Q":
                return False

        r=row-1
        c=col-1

        while r>=0 and c>=0:
            if arr[r][c]=="Q":
                return False
            r-=1
            c-=1

        r=row-1
        c=col+1

        while r>=0 and c<n:
            if arr[r][c]=="Q":
                return False
            r-=1
            c+=1

        return True


    def NQueen(self,n,row,arr,res):
        if row==n:
            res.append([''.join(i) for i in arr])
            return

        for col in range(n):
            # if self.isSafe(n,row,col,arr):
            #     arr[row][col]="Q"
            #     self.NQueen(n,row+1,arr,res)
            #     arr[row][col]="."

            arr[row][col]="Q"
            if self.isSafe(n,row,col,arr):
                self.NQueen(n,row+1,arr,res)
            arr[row][col]="."


    def solveNQueens(self, n: int) -> List[List[str]]:
        arr=[]
        for _ in range(n):
            arr.append(["."]*n)
        res=[]
        self.NQueen(n, 0, arr, res)
        return res

s=Solution().solveNQueens(int(input()))
print(s)

# O/P for 4 : [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
