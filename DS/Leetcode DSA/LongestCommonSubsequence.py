class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def solve(i,j):
            if i<0 or j<0:
                return 0
            if text1[i] == text2[j]:
                return 1+solve(i-1,j-1)
            res = max(solve(i-1,j), solve(i,j-1))
            return res
        return solve(len(text1)-1, len(text2)-1)