from collections import defaultdict
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited=[0]*n
        d=defaultdict(list)
        res=0
        prev=0
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        def dfs(i,connectedComponentCount):
            nonlocal visited
            visited[i]=True
            for j in d[i]:
                if not visited[j]:
                    connectedComponentCount[0]+=1
                    dfs(j,connectedComponentCount)
        for i in range(n):
            if not visited[i]:
                connectedComponentCount=[1]
                dfs(i,connectedComponentCount)
                res+=connectedComponentCount[0]*prev
                prev+=connectedComponentCount[0]
        return res
