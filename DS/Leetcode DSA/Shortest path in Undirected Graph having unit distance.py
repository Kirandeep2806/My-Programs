#!/usr/bin/python3

from collections import deque

class Solution:
    def shortestPath(self, edges, V, E, src):
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q = deque()
        vis = [0]*V
        dist = [1e9]*V
        dist[src] = 0
        # print(adj)
        q = deque([src])
        while q:
            node = q.popleft()
            # print(node)
            for i in adj[node]:
                if (dist[node] + 1 < dist[i]):
                    dist[i] = dist[node] + 1
                    q.append(i)

        for i in range(V):
            if dist[i] == 1e9:
                dist[i] = -1
        return dist


n,m = list(map(int, input().split()))
edges = eval(input())
src = int(input())
s = Solution().shortestPath(edges,n,m,src)
print(s)
