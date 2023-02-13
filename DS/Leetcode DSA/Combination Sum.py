from typing import List

class Solution:
	def findSolution(self,arr,i,target,ds,res):
		if target==0:
			res.append(ds.copy())
			return
		if i==len(arr):
			return
		if arr[i]<=target:
			ds.append(arr[i])
			self.findSolution(arr,i,target-arr[i],ds,res)
			ds.pop(-1)
		self.findSolution(arr,i+1,target,ds,res)

	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		ds=[]
		res=[]
		self.findSolution(candidates,0,target,ds,res)
		return res

s=Solution().combinationSum(eval(input()), int(input()))
print(s)
