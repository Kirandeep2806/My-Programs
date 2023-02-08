class Solution:
    def __init__(self):
        self.res=float("inf")

    def evaluation(self,arr,index,target,cnt):
        if index==target:
            self.res=min(self.res, cnt)
            return None

        if index>target:return None
        for i in range(1,arr[index]+1):
            self.evaluation(arr, index+i, target, cnt+1)

    def jump(self, nums) -> int:
        self.evaluation(nums, 0, len(nums)-1, 0)
        return self.res


s=Solution().jump(eval(input()))
print(s)