#!/usr/bin/python3

# Good explanation : https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/2858286/Python3-Hashmap-%2B-list-(Got-this-in-Google-phone-interview)

from collections import defaultdict
from random import choice

class RandomizedSet:
    def __init__(self):
        self.d=defaultdict(lambda:-1)
        self.l=[]

    def insert(self, val: int) -> bool:
        if self.d[val]!=-1:
            return False
        self.d[val]=self.l.__len__()
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if self.d[val]==-1:
            return False
        # print(self.l, self.d)
        self.d[self.l[-1]]=self.d[val]
        self.l[self.d[val]],self.l[-1]=self.l[-1],self.l[self.d[val]]
        self.d.pop(self.l.pop())
        return True

    def getRandom(self) -> int:
        return choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
