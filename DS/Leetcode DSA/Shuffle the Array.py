class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res


nums = list(map(int,input().split()))
n = int(input())

print(Solution().shuffle(nums,n))
