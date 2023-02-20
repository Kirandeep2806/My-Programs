"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        q=deque([root])
        vals=[]
        if root:
            res.append([root.val])
            temp=deque()
            while q:
                v=q.popleft()
                for i in v.children:
                    temp.append(i)
                    vals.append(i.val)
                if temp and not q:
                    q=temp.copy()
                    res.append(vals.copy())
                    vals=[]
                    temp.clear()
        return res

