#!/usr/bin/python3

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    	n=len(temperatures)
    	res=[0]*n
    	s=[]
    	for i,v in enumerate(temperatures):
    		while s and s[-1][1]<v:
			    popIndex=s.pop()[0]
			    res[popIndex]=i-popIndex
    		s.append([i,v])
    	return res

temperatures=[73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))
