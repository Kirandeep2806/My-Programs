from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        n=len(nums)
        for i in range(2**n):
            temp=[]
            cnt=n-1
            while i:
                if i&1:
                    temp.insert(0,nums[cnt])
                cnt-=1
                i>>=1
            res.add(tuple(temp))
        return res

s=Solution().subsetsWithDup(eval(input()))
print(s)
