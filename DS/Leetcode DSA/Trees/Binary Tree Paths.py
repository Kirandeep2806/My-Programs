# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []
        self.auxArr = []

    def isLeaf(self, node):
        return (node.left is None) and (node.right is None)

    def computation(self, root: Optional[TreeNode]) -> List[str]:
        if root:
            self.auxArr.append(str(root.val))
            if self.isLeaf(root):
                self.paths.append('->'.join(self.auxArr))
            self.computation(root.left)
            self.computation(root.right)
            self.auxArr.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.computation(root)
        return self.paths
