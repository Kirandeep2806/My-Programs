# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self,node):
        return node.left==None and node.right==None
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def solve(root):
            if self.isLeaf(root):
                return 1
            l = r = 100002
            if root.left!=None:
                l = solve(root.left)
            if root.right!=None:
                r = solve(root.right)
            return min(l,r)+1
        return solve(root)
