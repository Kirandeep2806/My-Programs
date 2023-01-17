#!/usr/bin/python3

class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.s2.clear()
        n=len(self.s1)
        for i in range(n):
            self.s2.append(self.s1[n-i-1])

    def pop(self) -> int:
        self.s1.clear()
        val=self.s2.pop()
        n=len(self.s2)
        for i in range(n):
            self.s1.append(self.s2[n-i-1])
        return val

    def peek(self) -> int:
        return self.s2[-1]

    def empty(self) -> bool:
        if self.s2:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
