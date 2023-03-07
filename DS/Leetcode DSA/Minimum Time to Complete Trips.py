from typing import List
import heapq as pq


class DS:
    def __init__(self,index,val):
        self.index=index
        self.val=val

    def __lt__(self,other):
        return self.val<other.val

    def __str__(self):
        return f"{self.index},{self.val}"

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        prev=0
        minTime=0
        l=[]
        for index,val in enumerate(time):
            pq.heappush(l,DS(index,val))
        while totalTrips!=0:
            ds=pq.heappop(l)
            minTime+=(ds.val-prev)
            prev=ds.val
            pq.heappush(l, DS(ds.index,prev+time[ds.index]))
            totalTrips-=1
        return minTime


s=Solution().minimumTime(eval(input()), int(input()))
print(s)
