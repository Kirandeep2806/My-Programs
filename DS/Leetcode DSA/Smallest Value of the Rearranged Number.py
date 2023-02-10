class Solution:
    def smallestNumber(self, num: int) -> int:
        strnum=list(str(num))
        if num>0:
            l=sorted(strnum)
            n=len(l)
            for i in range(n):
                if l[i]!="0":break
            res=""
            res=l[i]+"0"*i+(''.join(l[i+1:]) if i<n-1 else "")
        else:
            res=strnum[0]+''.join(sorted(strnum[1:],reverse=True))
        return int(res)

s=Solution().smallestNumber(int(input()))
print(s)
