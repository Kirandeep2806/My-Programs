from __future__ import annotations

def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = tot = 0
    res = len(nums) + 1
    for right, num in enumerate(nums):
        tot += num
        while left <= right and tot >= target:
            res = min(res, right - left + 1)
            tot -= nums[left]
            left += 1
            
    return 0 if res == len(nums) + 1 else res

print(minSubArrayLen(7, [2,3,1,2,4,3]))