from typing import List

class Solution:
    def findSolution(self,index,candidates,target,ds,res):
        if target==0:
            res.append(ds.copy())
            return

        if index==len(candidates) or target<0:
            return

        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue

            if target-candidates[i]>=0:
                ds.append(candidates[i])
                self.findSolution(i+1, candidates, target-candidates[i], ds, res)
                ds.pop()
            else:
                break


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ds=[]
        res=[]
        self.findSolution(0,sorted(candidates),target,ds,res)
        return res

s=Solution().combinationSum2(eval(input()), int(input()))
print(s)
