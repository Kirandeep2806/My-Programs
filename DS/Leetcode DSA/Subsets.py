from typing import List

class Solution:
	def soln(self,i,nums,ds,res):
		if i==nums.__len__():
			res.append(ds.copy())
			return

		ds.append(nums[i])
		self.soln(i+1, nums, ds, res)
		ds.pop(-1)
		self.soln(i+1, nums, ds, res)

	def subsets(self, nums: List[int]) -> List[List[int]]:
		res=[]
		ds=[]
		self.soln(0,nums,ds,res)
		return res

s=Solution().subsets(eval(input()))
print(s)
