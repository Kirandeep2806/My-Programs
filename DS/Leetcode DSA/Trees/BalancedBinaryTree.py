# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def computeHeight(self, root):
        if root is None:
            return 0
        lh = self.computeHeight(root.left)
        rh = self.computeHeight(root.right)
        if abs(lh-rh)>1 or (lh==-1) or (rh==-1):
            return -1
        return 1+max(lh, rh)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return True if self.computeHeight(root)>-1 else False
