# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        self.maxDia = max(lh+rh, self.maxDia)
        return 1+max(lh, rh)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDia = 0
        self.maxDepth(root)
        return self.maxDia
