from typing import List

class Solution:
    def findSolution(self,i,candidates,target,ds,res):
        if target==0:
            res.add(tuple(ds))
            return True

        if target<0 or i==len(candidates):
            return False

        ds.append(candidates[i])
        resp1=self.findSolution(i+1, candidates, target-candidates[i], ds, res)
        ds.pop(-1)

        resp2=self.findSolution(i+1, candidates, target, ds, res)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ds=[]
        res=set()
        self.findSolution(0,sorted(candidates),target,ds,res)
        return res

s=Solution().combinationSum2(eval(input()), int(input()))
print(s)
