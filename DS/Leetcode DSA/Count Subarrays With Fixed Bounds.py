from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n=len(nums)
        minLocal=float("inf")
        maxLocal=-minLocal
        i=0
        j=0
        res=0

        if minK==maxK:
            consecutiveCount=[0]*n
            if nums[0]==minK:
                consecutiveCount[0]=1
            for k in range(1,n):
                if nums[k]==minK:
                    consecutiveCount[k]=consecutiveCount[k-1]+1
                else:
                    res+=((consecutiveCount[k-1])*(consecutiveCount[k-1]+1))//2
            if consecutiveCount[n-1]!=0:
                res+=((consecutiveCount[n-1])*(consecutiveCount[n-1]+1))//2

        else:
            while i<n and j<n:
                print(i,j)
                if i<=j:
                    minLocal=min(minLocal, nums[i], nums[j])
                    maxLocal=max(maxLocal, nums[i], nums[j])
                    if minLocal==minK and maxLocal==maxK:
                        res+=1
                    elif minLocal!=minK and maxLocal!=maxK:
                        i+=1
                    else: # elif (minLocal!=minK and maxLocal==maxK) or (minLocal==minK and maxLocal!=maxK):
                        if i<j:
                            i+=1
                            continue
                    j+=1
                else:
                    j+=1
        return res



minK=int(input())
maxK=int(input())
print(Solution().countSubarrays(eval(input()), minK, maxK))
