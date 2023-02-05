from collections import Counter

class Solution:
    def addElement(self, ele, d):
        if d.get(ele,0):
            d[ele]+=1
        else:
            d[ele]=1

    def delElement(self, ele,d):
        d[ele]-=1
        if d[ele]==0:
            del d[ele]


    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n>m:
            return False
        d1,d2={},{}
        for i in range(n):
            self.addElement(s1[i], d1)
            self.addElement(s2[i], d2)
        for i in range(i+1,m):
            if d1==d2:
                return True
            self.addElement(s2[i], d2)
            self.delElement(s2[i-n], d2)
        else:
            if d1==d2:
                return True
        return False


s1=input()
s2=input()
s = Solution().checkInclusion(s1, s2)
print(s)
