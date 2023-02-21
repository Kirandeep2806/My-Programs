class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        n=nums.__len__()
        high=n
        i=0
        while low<=high:
            mid=low+(high-low)//2
            if mid==n-1:
                return nums[n-1]
            if nums[mid]==nums[mid^1]:
                low=mid+1
            else:
                i=mid
                high=mid-1
        return nums[i]
