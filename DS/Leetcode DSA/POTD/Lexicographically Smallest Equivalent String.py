#!/usr/bin/python3

from collections import defaultdict, OrderedDict

class Solution:
	def DFSMap(self, node, map, adj, visited):
		if node not in visited:
			visited.add(node)
			for i in adj[node]:
				map[node]=min(map[node] or "z", node, self.DFSMap(i, map, adj, visited))
			return map[node]
		else:
			return map[node] or node

	def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
		referenceMap = defaultdict(set)
		d=OrderedDict()
		n=len(s1)
		for i in range(n):
			referenceMap[s2[i]].add(s1[i])
			referenceMap[s1[i]].add(s2[i])
		for j in sorted(referenceMap.items(),key=lambda x:x[0]):
			d[j[0]]=j[1]

		# print(d)
		m=defaultdict(lambda:None)
		visited=set()
		for i in d:
			if i not in visited:
				self.DFSMap(i,m,d,visited)

		res=""
		# print(d)
		print(m)
		for i in baseStr:
			res+=(m[i] or i)
		return res


if __name__ == "__main__":
	s1=input()
	s2=input()
	baseStr=input()
	s=Solution().smallestEquivalentString(s1, s2, baseStr)
	print(s)
