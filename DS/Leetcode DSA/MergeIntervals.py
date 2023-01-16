#!/usr/bin/python3

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=0
        intervals.sort(key=lambda x:x[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]<=intervals[res][1]:
                intervals[res][0]=min(intervals[res][0],intervals[i][0])
                intervals[res][1]=max(intervals[res][1],intervals[i][1])
            else:
                res+=1
                intervals[res]=intervals[i]
        return intervals[:res+1]

