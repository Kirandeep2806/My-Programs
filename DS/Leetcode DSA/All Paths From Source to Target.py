class Solution:
    def DFS(self,n,graph,node,visited,temp,res):
        visited[node]=True
        temp.append(node)
        if node==n-1:
            res.append(temp.copy())
            return
        for i in range(n):
            if graph[node][i] and visited.get(i,False)==False:
                self.DFS(n,graph,i,visited,temp,res)
                temp.pop(-1)
            visited[i]=False
        


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=graph.__len__()
        start=0
        res=[]
        visited={}
        adj=[]
        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append(0)
            adj.append(temp)

        for i in range(n):
            temp=[]
            for j in graph[i]:
                adj[i][j]=1

        self.DFS(n,adj,0,visited,[],res)
        return res