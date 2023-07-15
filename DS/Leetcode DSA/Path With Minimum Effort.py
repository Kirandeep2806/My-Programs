import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights) # rows
        n = len(heights[0]) # cols
        dist = [[1e9 for _ in range(n)] for __ in range(m)]
        dist[0][0] = 0
        pq = [(0,(0,0))]
        dr = [0,0,-1,1]
        dc = dr[::-1]
        while pq:
            diff, (x, y) = heapq.heappop(pq)
            if x==m-1 and y==n-1:
                return diff
            for i in range(4):
                newx = x+dr[i]
                newy = y+dc[i]
                if 0<=newx<m and 0<=newy<n:
                    newEffort = max(abs(heights[x][y] - heights[newx][newy]), diff)
                    if newEffort < dist[newx][newy]:
                        dist[newx][newy] = newEffort
                        heapq.heappush(pq, (dist[newx][newy], (newx, newy)))
        return 0
