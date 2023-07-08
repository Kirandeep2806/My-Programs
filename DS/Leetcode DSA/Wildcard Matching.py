class Solution:
    def isMatch(self, s: str, t: str) -> bool:
        @lru_cache(None)
        def solve(i,j):
            if i<0 and j<0:
                return True
            if i>=0 and j<0:
                return False
            if i<0 and j>=0:
                for k in range(j+1):
                    if t[k]!="*":
                        return False
                return True
            if s[i]==t[j] or t[j]=="?":
                return solve(i-1, j-1)
            if t[j]=="*":
                return solve(i,j-1) or solve(i-1,j)
            return False
        return solve(len(s)-1, len(t)-1)
