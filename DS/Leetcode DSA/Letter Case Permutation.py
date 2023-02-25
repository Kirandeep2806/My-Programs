class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def perm(i,arr,temp):
            if i==n:
                res.append(''.join(temp))
                return
            if arr[i].isalpha():
                temp.append(arr[i].upper())
                perm(i+1,arr,temp)
                temp.pop()
            temp.append(arr[i].lower())
            perm(i+1,arr,temp)
            temp.pop()

        n=len(s)
        arr=list(s)
        res=[]
        perm(0,arr,[])
        return res
