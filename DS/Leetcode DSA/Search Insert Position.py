from typing import List

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		low=0
		high=nums.__len__()-1
		res=0
		if target>nums[high]:
			return high+1
		while low<=high:
			# mid=(low+high)//2 : Overflow mi8 occur
			# mid=low+(high-low)//2 : No Overflow
			# Below also No overflow
			mid=(low&high)+((low^high)>>1)
			if nums[mid]>=target:
				res=mid
				high=mid-1
			else:
				low=mid+1
		return res




s=Solution().searchInsert(eval(input()),int(input()))
print(s)