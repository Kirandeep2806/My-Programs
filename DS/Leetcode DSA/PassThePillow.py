class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i=time//(n-1)
        res=time%(n-1)
        if i&1:
            return n-res
        else:
            return res+1
        