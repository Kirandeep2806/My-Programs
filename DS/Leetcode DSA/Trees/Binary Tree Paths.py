# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.


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
