from typing import List
from math import ceil

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n=len(seats)
        index=0
        consecutives=1
        m=1
        start=0
        for i in range(1,n):
            if seats[i]==0:
                if seats[i]==seats[i-1]:
                    index+=1
                    consecutives+=1
            else:
                if m==index+1:
                    start=m
                consecutives=1
            if consecutives>=m:
                    index=i
                    m=consecutives
        return max(consecutives, start, ceil(m/2))

s=Solution().maxDistToClosest(eval(input()))
print(s)
