from typing import List

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        ways=0
        def dfs(index, target, types):
            nonlocal ways

            if target==0:
                ways+=1
                return
            elif target<0:
                return

            for i in range(index, len(types)):
                for j in range(1, types[i][0]+1):
                    if types[i][0]>0:
                        if target-j*types[i][1]<0:
                            break
                        dfs(i+1, target-j*types[i][1], types)

        dfs(0, target, types)
        return ways


s=Solution().waysToReachTarget(int(input()),eval(input()))
print(s)
