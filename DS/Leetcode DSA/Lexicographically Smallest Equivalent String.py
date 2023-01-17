#!/usr/bin/python3

from collections import defaultdict, OrderedDict

class Solution:
	def DFSMap(self, node, mp, adj, visited, least="z"):
		least = min(least, mp[node] or node)
		if node not in visited:
			visited.add(node)
			for i in adj[node]:
				least = self.DFSMap(i, mp, adj, visited, least)
		mp[node] = least
		return least

	def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
		referenceMap = defaultdict(set)
		d=OrderedDict()
		n=len(s1)
		for i in range(n):
			referenceMap[s2[i]].add(s1[i])
			referenceMap[s1[i]].add(s2[i])
		for j in sorted(referenceMap.items(),key=lambda x:x[0]):
			d[j[0]]=j[1]

		del referenceMap

		m=defaultdict(lambda:None)
		visited=set()
		for i in d:
			if i not in visited:
				self.DFSMap(i,m,d,visited)

		res=""
		# print(m)
		for i in baseStr:
			res+=(m[i] or i)
		return res


if __name__ == "__main__":
	s1=input()
	s2=input()
	baseStr=input()
	s=Solution().smallestEquivalentString(s1, s2, baseStr)
	print(s)
