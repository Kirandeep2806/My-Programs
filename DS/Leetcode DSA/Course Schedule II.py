class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for a,b in prerequisites:
            indegree[a] += 1
            d[b].append(a)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for i in d[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return topo if len(topo) == numCourses else []
