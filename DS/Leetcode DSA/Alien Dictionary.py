from collections import deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        adj = [[] for _ in range(K)]
        for i in range(N-1):
            n = min(len(alien_dict[i]), len(alien_dict[i+1]))
            ptr = 0
            while ptr<n:
                if alien_dict[i][ptr] != alien_dict[i+1][ptr]:
                    u = ord(alien_dict[i][ptr]) - 97
                    v = ord(alien_dict[i+1][ptr]) - 97
                    adj[u].append(v)
                    break
                ptr += 1
        indegree = [0]*K
        for i in range(K):
            for j in adj[i]:
                indegree[j] += 1
        q = deque()
        for i in range(K):
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
        topo = list(map(lambda x:chr(97+x), topo))
        order = ''.join(topo)
        return order

s = Solution()
N, K = list(map(int, input().split()))
d = input().split()
res = s.findOrder(d, N, K)
print(res)
