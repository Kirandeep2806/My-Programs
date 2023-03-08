from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateTime(potentialK):
            nonlocal h,piles
            time=0
            for i in piles:
                time+=ceil(i/potentialK)
                if time>h: # Time is high means denominator is too low, Denominator means potentialK - So we need to increase the value of the potentialK/Estimated K value
                    return True
            return False

        low=1
        high=max(piles)
        while low<=high:
            mid=low+(high-low)//2
            if calculateTime(mid):
                low=mid+1
            else:
                high=mid-1
        return low
        
s=Solution().minEatingSpeed(eval(input()), int(input()))
print(s)
