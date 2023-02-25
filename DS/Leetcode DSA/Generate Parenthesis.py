class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(s,openCount,closeCount):
            if len(s)==n*2:
                res.append(s)
                return
            if openCount<n:
                dfs(s+"(",openCount+1,closeCount)
            if closeCount<openCount:
                dfs(s+")",openCount,closeCount+1)

        res=[]
        dfs("",0,0)
        return res
