from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n=len(nums)
        nums.sort()
        res=0
        for index in range(n-1):
            i=bisect_left(nums,lower-nums[index],lo=index+1,hi=n)
            j=bisect_right(nums,upper-nums[index],lo=index+1,hi=n)
            res+=(j-i)
        return res

s=Solution().countFairPairs(eval(input()),int(input()),int(input()))
print(s)
