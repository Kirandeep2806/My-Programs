from collections import defaultdict

class Solution:
    def __init__(self):
        self.res=float("inf")

    def evaluation(self,arr,index,target,cnt,memset):
        if index==target:
            return cnt
        if index in memset:
            return memset[index]
        if index>target:
            return float("inf")
        for i in range(1,arr[index]+1):
            memset[index]=min(memset[index],self.evaluation(arr, index+i, target, cnt+1, memset))
            print(memset[index])
            self.res=min(self.res, cnt+memset[i])
        return self.res

    def jump(self, nums) -> int:
        d=defaultdict(lambda:float("inf"))
        self.evaluation(nums, 0, len(nums)-1, 0,d)
        print(d)
        return self.res

s=Solution().jump(eval(input()))
print(s)
