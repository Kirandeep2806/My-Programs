#!/usr/bin/python3

from typing import List

class Solution:
	def __init__(self):
		self.stack = []

	def topoSort(self, V, adj):
		vis = [0]*V
		def dfs(node):
			vis[node] = 1
			for i,wt in adj[node]:
				if vis[i] == 0:
					dfs(i)
			self.stack.append(node)
		for i in range(V):
			if vis[i] == 0:
				dfs(i)

	def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
		adj = [[] for _ in range(n)]
		for u,v,wt in edges:
			adj[u].append((v,wt))
		self.topoSort(n, adj)
		dist = [1e9]*n # Always put this as max or min value like -1e9 or 1e9 but not -1
		dist[0] = 0
		while self.stack:
			node = self.stack.pop()
			for i,wt in adj[node]:
				dist[i] = min(dist[i], dist[node] + wt)
		for i in range(n):
		    if dist[i] == 1e9:
		        dist[i] = -1
		return dist


n,m = list(map(int, input().split()))
edge = eval(input())
s = Solution().shortestPath(n,m,edge)
print(s)

