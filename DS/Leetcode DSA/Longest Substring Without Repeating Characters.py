#!/usr/bin/python3

from collections import defaultdict
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		n=len(s)
		d=defaultdict(lambda:-1) #imp
		res=i=0
		for j in range(n):
			i=max(i, d[s[j]]+1) # VVVImp
			maxEnd=j-i+1
			res=max(maxEnd, res)
			d[s[j]]=j
		return res

s=Solution().lengthOfLongestSubstring(input())
print(s)
