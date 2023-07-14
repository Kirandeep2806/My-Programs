import heapq

class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dist = [1e9]*V
        dist[S] = 0
        pq = []
        # print(adj)
        heapq.heappush(pq, (0, S))
        while pq:
            distanceCovered, node = heapq.heappop(pq)
            for i in adj[node]:
                nextNode, curToNext = i
                if dist[node] + curToNext < dist[nextNode]:
                    dist[nextNode] = dist[node] + curToNext
                    pq.append((dist[nextNode], nextNode))
        return dist
