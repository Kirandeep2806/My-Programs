from typing import List

class Solution:
    def soln(self,index,n,nums,res):
        if index==n:
            res.append(nums.copy())
            return

        for i in range(index,n):
            nums[i],nums[index]=nums[index],nums[i]
            self.soln(index+1,n,nums,res)
            nums[i],nums[index]=nums[index],nums[i]
 

    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.soln(0,len(nums),nums,res)
        return res

s=Solution().permute(eval(input()))
print(s)
