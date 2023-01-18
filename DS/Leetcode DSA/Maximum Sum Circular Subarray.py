#!/usr/bin/python3

from typing import List
class Solution:
	def kadane(self,arr):
		res=-float("inf")
		s=0
		for i in arr:
			s+=i
			res=max(s, res)
			s=max(s, 0)
		return res

	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		psum=self.kadane(nums)
		if psum<=0:
			return psum
		s=0
		for i in range(len(nums)):
			s+=nums[i]
			nums[i]=-nums[i]
		nsum=s+self.kadane(nums)
		return max(psum,nsum)

nums=list(map(int,input().split()))
s=Solution().maxSubarraySumCircular(nums)
print(s)
