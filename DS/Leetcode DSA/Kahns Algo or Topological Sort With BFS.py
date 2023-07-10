from collections import deque

class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        indegree = [0]*V
        for i in range(V):
            for node in adj[i]:
                indegree[node] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        # print(topo)
        return topo
