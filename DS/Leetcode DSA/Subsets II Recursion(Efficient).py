from typing import List

class Solution:
    def recurSoln(self,index,n,nums,ds,res):
        res.append(ds.copy())
        for i in range(index,n):
            if i!=index and nums[i]==nums[i-1]:continue
            ds.append(nums[i])
            self.recurSoln(i+1,n,nums,ds,res)
            ds.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ds=[]
        res=[]
        self.recurSoln(0,len(nums),nums,ds,res)
        return res


s=Solution().subsetsWithDup(eval(input()))
print(s)
