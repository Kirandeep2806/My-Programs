from typing import List

class Solution:
    def isSafe(self,n,row,col,arr,d):
        for i in d:
            if (d[i]==col) or (abs(row-i)==abs(col-d[i])):
                return False
        return True

    def NQueen(self,n,row,arr,res,d={}):
        if row==n:
            res.append([''.join(i) for i in arr])
            return

        for col in range(n):
            arr[row][col]="Q"
            if self.isSafe(n,row,col,arr,d):
                d[row]=col
                self.NQueen(n,row+1,arr,res,d)
                del d[row]
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