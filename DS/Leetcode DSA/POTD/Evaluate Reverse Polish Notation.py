#!/usr/bin/python3

from math import ceil, floor

class Solution:
    def __init__(self):
        self.s=[]
        self.operands={"+","*","/","-"}

    def evalRPN(self, tokens) -> int:
        for i in tokens:
            if i in self.operands:
                v1=str(self.s.pop())
                v2=str(self.s.pop())
                val=eval(v2+i+v1)
                val=ceil(val) if val<0 else floor(val)
                self.s.append(val)
            else:
                self.s.append(int(i))
        return self.s[0]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))
