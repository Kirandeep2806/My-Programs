from typing import List

class Solution:
	def findCombinations(self,pos,k,target,cnt,ds,res):
		if cnt==k and target==0:
			res.append(ds.copy())
			return

		for i in range(pos,10):
			if (target-i)>=0:
				ds.append(i)
				self.findCombinations(i+1, k, target-i, cnt+1, ds, res)
				ds.pop(-1)

	def combinationSum3(self, k: int, n: int) -> List[List[int]]:
		ds=[]
		res=[]
		self.findCombinations(1,k,n,0,ds,res)
		return res

s=Solution().combinationSum3(int(input()),int(input()))
print(s)