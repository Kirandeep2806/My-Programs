class Solution:
    def countArrangement(self, n: int) -> int:
        cnt=0
        def perm(i,arr):
            nonlocal cnt
            if i==n:
                cnt+=1
                return
            for j in range(i,n):
                if (arr[j]%(i+1)==0) or ((i+1)%arr[j])==0:
                    arr[i],arr[j]=arr[j],arr[i]
                    perm(i+1,arr)
                    arr[i],arr[j]=arr[j],arr[i]

        arr=[i for i in range(1,n+1)]
        perm(0,arr)
        return cnt
        