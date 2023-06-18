class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1]*V
        # def bfs(start):
        #     q = deque([start])
        #     color[start] = 0
        #     while q:
        #         node = q.popleft()
        #         for i in graph[node]:
        #             if color[i] == -1:
        #                 color[i] = int(not color[node])
        #                 q.append(i)
        #             elif color[i] == color[node]:
        #                 return False
        #     return True
        # for i in range(V):
        #     if color[i] == -1:
        #         if bfs(i) == False:
        #             return False
        # return True

        def dfs(node, col):
            color[node] = col
            for i in graph[node]:
                if color[i] == -1:
                    if dfs(i, int(not color[node])) == False:
                        return False
                elif color[i] == col:
                    return False
            return True
            
        for i in range(V):
            if color[i] == -1:
                if dfs(i,-1) == False:
                    return False
        return True

