#!/usr/bin/python3

from typing import List
from collections import Counter

class Solution:
	def minimumRounds(self, tasks: List[int]) -> int:
		c=Counter(tasks)
		res=0
		for i in c:
			if c[i]==1:
				return -1
			rem=c[i]%3
			if rem==0:
				res+=c[i]//3
			elif rem==1:
				res+=(c[i]-4)//3+2
			else:
				res+=(c[i]-2)//3+1
		return res


tasks = list(map(int,input().split()))
res=Solution().minimumRounds(tasks)
print(res)
