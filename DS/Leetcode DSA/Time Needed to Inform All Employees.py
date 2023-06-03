from collections import defaultdict
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = defaultdict(list)
        for i in range(n):
            d[manager[i]].append(i)
        def solve(node):
            if d[node]:
                m = 0
                for i in d[node]:
                    m = max(m, solve(i) + informTime[node])
                return m
            return 0
        return solve(headID)
