# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        q = deque([root])
        maxSum = -float("inf")
        cnt = 0
        while q:
            cnt += 1
            s = 0
            for i in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > maxSum:
                maxSum = s
                level = cnt
        return level
