from collections import deque

# Using Kahn's Algorithm

class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
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
        return not(len(topo) == V)
