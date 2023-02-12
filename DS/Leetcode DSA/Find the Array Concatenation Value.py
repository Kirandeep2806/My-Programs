from typing import List
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        i,j=0,n-1
        while i<=j:
            if i==j:
                res+=nums[i]
                i+=1
                j-=1
                continue
            res+=int(str(nums[i])+str(nums[j]))
            i+=1
            j-=1
        return res



s=Solution().findTheArrayConcVal(eval(input()))
print(s)
