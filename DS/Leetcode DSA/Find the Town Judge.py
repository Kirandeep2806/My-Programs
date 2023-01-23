from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d=defaultdict(set)
        for i in trust:
            d[i[0]].add(i[1])
        t=set([i for i in range(1,n+1)])
        cnt=0
        for i in d:
            cnt+=1
            t&=d[i]
        if cnt==n-1 and len(t)==1:
            val=list(t)[0]
            if d[val]:
                return -1
            return val
        return -1

n=int(input())
l=eval(input())
s=Solution()
print(s.findJudge(n, l))
