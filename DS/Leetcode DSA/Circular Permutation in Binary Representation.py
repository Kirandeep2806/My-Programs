from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res=[start]
        def XORAndPower2(a,b):
            num=a^b
            if num and (num&(num-1)==0):
                return True
            return False

        def validPerm(curr,cnt,arr):
            nonlocal res
            if cnt==0:
                if XORAndPower2(res[0],res[-1]):
                    return True
                return False

            for i in arr:
                if XORAndPower2(curr,i):
                    res.append(i)
                    if validPerm(i,cnt-1,arr-{i}):
                        return True
                    res.pop()

        arr=set([i for i in range(2**n) if i!=start])
        validPerm(start,2**n-1,arr)
        return res

s=Solution().circularPermutation(int(input()), int(input()))
print(s)