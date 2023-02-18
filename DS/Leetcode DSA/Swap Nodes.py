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
        if root.left and root.right:
            root.left.val,root.right.val=root.right.val,root.left.val
        elif root.right:
            root.left=TreeNode(root.right.val)
            root.right=None
        elif root.left:
            root.right=TreeNode(root.left.val)
            root.left=None

    def swapNodes(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root
