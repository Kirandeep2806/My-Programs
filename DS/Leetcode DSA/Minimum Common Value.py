from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)
        i=j=0
        found=False
        while i<m and j<n:
            if nums1[i]==nums2[j]:
                found=True
                break
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        if not found:
            return "-1"
        return nums1[i]

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
s=Solution().getCommon(nums1, nums2)
print(s)
