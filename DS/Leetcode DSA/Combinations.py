from typing import List

class Solution:
    def findCombinations(self,pos,n,k,cnt,ds,res):
        if cnt==k:
            res.append(ds.copy())
            return

        for i in range(pos,n+1):
            ds.append(i)
            self.findCombinations(i+1, n, k, cnt+1, ds, res)
            ds.pop(-1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        ds=[]
        res=[]
        self.findCombinations(1, n, k, 0, ds, res)
        return res

s=Solution().combine(int(input()),int(input()))
print(s)
