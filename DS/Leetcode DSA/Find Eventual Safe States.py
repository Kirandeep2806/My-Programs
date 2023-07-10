class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        check = [0]*V
        vis = [0]*V
        pathVis = [0]*V

        def dfs(node):
            vis[node] = 1
            pathVis[node] = 1

            for i in graph[node]:
                if vis[i] == 0:
                    if dfs(i) == True:
                        return True
                elif pathVis[i] == 1:
                    return True
            pathVis[node] = 0
            check[node] = 1
            return False

        for i in range(V):
            if vis[i] == 0:
                print(i)
                dfs(i)

        safe = []
        for i in range(V):
            if check[i] == 1:
                safe.append(i)
        return safe

# Using Topological Sorting through Kahn's Algorithm

# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         V = len(graph)
#         revGraph = [[] for _ in range(V)]
#         for ind, adj in enumerate(graph):
#             for node in adj:
#                 revGraph[node].append(ind)
#         indegree = [0]*V
#         for i in range(V):
#             for node in revGraph[i]:
#                 indegree[node] += 1
#         q = deque()
#         for i in range(V):
#             if indegree[i] == 0:
#                 q.append(i)
#         topo = []
#         while q:
#             node = q.popleft()
#             topo.append(node)
#             for i in revGraph[node]:
#                 indegree[i] -= 1
#                 if indegree[i] == 0:
#                     q.append(i)
#         return sorted(topo)
