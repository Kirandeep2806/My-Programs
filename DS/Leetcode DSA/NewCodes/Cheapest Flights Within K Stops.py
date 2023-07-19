from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        dist = [float("inf")]*n
        dist[src] = 0
        for u,v,cost in flights:
            adj[u].append((v, cost))
        # k, node, distance till
        q = deque([(0,src,0)])
        while q:
            stops, node, distanceCovered = q.popleft()
            if stops > k:
                continue
            for nextNode, cost in adj[node]:
                if distanceCovered + cost < dist[nextNode]:
                    dist[nextNode] = distanceCovered + cost
                    q.append((stops+1, nextNode, dist[nextNode]))
        return -1 if dist[dst]==float("inf") else dist[dst]
