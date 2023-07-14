import heapq

class Solution:
    def shortestPath(self, V, E, edges):
        adj = [[] for _ in range(V+1)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        dist = [1e9]*(V+1)
        parent = [i for i in range(V+1)]
        dist[1] = 0
        pq = []
        heapq.heappush(pq, (0, 1))
        while pq:
            distanceCovered, node = heapq.heappop(pq)
            for i in adj[node]:
                nextNode, curToNext = i
                if dist[node] + curToNext < dist[nextNode]:
                    dist[nextNode] = dist[node] + curToNext
                    pq.append((dist[nextNode], nextNode))
                    parent[nextNode] = node
        if dist[V] == 1e9:
            return [-1]
        path = []
        node = V
        while node!=1:
            path.append(node)
            node = parent[node]
        path.append(1)
        return path[::-1]
