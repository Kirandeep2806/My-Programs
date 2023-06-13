from copy import deepcopy
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s = defaultdict(int)
        for i in range(n):
            s[tuple(grid[i])] += 1
        transpose = deepcopy(grid)
        for i in range(n):
            for j in range(n):
                transpose[j][i] = grid[i][j]
        res = 0
        print(transpose)
        for i in transpose:
            res += s[tuple(i)]
        return res