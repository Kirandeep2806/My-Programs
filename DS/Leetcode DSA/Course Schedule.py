class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for a,b in prerequisites:
            indegree[a] += 1
            d[b].append(a)
        # print(d)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        # print(q)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for i in d[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        # print(topo)
        return len(topo) == numCourses
