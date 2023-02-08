from collections import defaultdict

class Solution:
    def evaluation(self,arr,index,target,memset):
        if index==target:return 0
        if index in memset:return memset[index]
        if index>target:return float("inf")
        for i in range(1,arr[index]+1):
            memset[index]=min(memset[index],self.evaluation(arr,index+i,target,memset)+1)
        return memset[index]

    def jump(self, nums) -> int:
        d=defaultdict(lambda:float("inf"))
        return self.evaluation(nums,0,len(nums)-1,d)

s=Solution().jump(eval(input()))
print(s)
