#!/usr/bin/python3

from typing import List

class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		inserted=False
		res=0
		n=len(intervals)
		for i in range(1,n):
			if intervals[i][0]<=intervals[res][1]:
				intervals[res][0]=min(intervals[res][0], intervals[i][0])
				intervals[res][1]=max(intervals[res][1], intervals[i][1])
			else:
				res+=1
		return intervals[:res+1]


if __name__=="__main__":
	intervals = eval(input())
	newInterval = eval(input())
	s=Solution().insert(intervals, newInterval)
	print(s)