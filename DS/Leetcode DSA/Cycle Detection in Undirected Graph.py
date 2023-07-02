from typing import List
from collections import deque

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis=[0]*V
        def bfs(node,vis):
            q = deque([(node,-1)])
            while q:
                node, parent = q.popleft()
                vis[node] = 1
                for i in adj[node]:
                    if vis[i]==0:
                        q.append((i,node))
                    else:
                        if i!=parent:
                            return True
            return False
        for i in range(V):
            if vis[i]==0:
                if bfs(i,vis):
                    return True
        return False
