#!/usr/bin/python3

from typing import List

class Solution:
	def compute(self,mat,n,m):
		if n>=0 and m>=0:
			try:
				if mat[n][m]:
					return 1
			except:
				pass
		return 0

	def gameOfLife(self, board: List[List[int]]) -> None:
		cpy=[row[:] for row in board]
		n=len(board)
		m=len(board[0])
		for i in range(n):
			for j in range(m):
				cnt=0
				cnt+=self.compute(cpy, i-1, j-1)
				cnt+=self.compute(cpy, i-1, j)
				cnt+=self.compute(cpy, i-1, j+1)
				cnt+=self.compute(cpy, i, j-1)
				cnt+=self.compute(cpy, i, j+1)
				cnt+=self.compute(cpy, i+1, j-1)
				cnt+=self.compute(cpy, i+1, j)
				cnt+=self.compute(cpy, i+1, j+1)

				if cpy[i][j]==1:
					if cnt<2:
						board[i][j]=0
					elif cnt==2 or cnt==3:
						board[i][j]=1
					elif cnt>3:
						board[i][j]=0
				else:
					if cnt==3:
						board[i][j]=1
		return board
				


board = eval(input())
res = Solution().gameOfLife(board)
print(res)
