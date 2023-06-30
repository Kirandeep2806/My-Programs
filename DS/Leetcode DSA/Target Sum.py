# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         @cache
#         def solve(i, tar):
#             if i == 0:
#                 if nums[0] == 0 and tar == 0:
#                     return 2
#                 if tar == nums[0] or tar == -nums[i]:
#                     return 1
#                 return 0
#             minus = solve(i-1, tar-nums[i])
#             plus = solve(i-1, tar+nums[i])
#             return plus + minus
#         return solve(len(nums)-1, target)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def solve(i, tar):
            if i == 0:
                if nums[0] == 0 and tar == 0:
                    return 2
                if nums[0] == tar or tar == 0:
                    return 1
                return 0
            notpick = solve(i-1, tar)
            pick = 0
            if nums[i] <= tar:
                pick = solve(i-1, tar-nums[i])
            return notpick + pick
        s = sum(nums)
        s2 = s - target
        if (-s<=target<=s) and (s2%2==0):
            return solve(len(nums)-1, s2//2)
        return 0
