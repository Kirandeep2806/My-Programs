from functools import lru_cache
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        @lru_cache(None)
        def solve(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if s[i] == t[j]:
                return solve(i-1,j-1)
            else:
                insert = solve(i,j-1)
                delete = solve(i-1,j)
                replace = solve(i-1,j-1)
                return min(insert, delete, replace)+1
        return solve(len(s)-1, len(t)-1)
