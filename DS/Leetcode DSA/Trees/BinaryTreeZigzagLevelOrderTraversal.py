# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def __init__(self):
        self.LtoR = True
        self.res = []

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            d = deque()
            d.append(root)
            while d.__len__():
                temp = d.copy()
                aux = deque()
                levelRes = deque()
                while temp.__len__()!=0:
                    ele = temp.popleft()
                    if self.LtoR:
                        levelRes.append(ele.val)
                    else:
                        levelRes.appendleft(ele.val)
                    if ele.left is not None:
                        aux.append(ele.left)
                    if ele.right is not None:
                        aux.append(ele.right)
                self.res.append(levelRes)
                d = aux
                self.LtoR = not self.LtoR
        return self.res

