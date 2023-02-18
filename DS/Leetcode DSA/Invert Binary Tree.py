# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,root):
        if root is None:
            return
        self.traversal(root.left)
        self.traversal(root.right)
        root.left,root.right=root.right,root.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root