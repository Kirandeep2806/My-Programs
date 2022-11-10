from queue import LifoQueue

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = LifoQueue()
        for i in s:
            if stack.qsize()!=0:
                tos = stack.get()
                if tos != i:
                    stack.put(tos)
                    stack.put(i)
            else:
                stack.put(i)
        res = ""
        while stack.qsize()!=0:
            res = stack.get() + res
        return res


s = Solution()
res = s.removeDuplicates(input())
print(res)
