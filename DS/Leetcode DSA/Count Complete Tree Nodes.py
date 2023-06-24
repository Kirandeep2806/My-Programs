# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countHeightLeft(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        def countHeightRight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        def solve(node):
            lh = countHeightLeft(node)
            rh = countHeightRight(node)
            if lh == rh:
                return (1<<lh)-1
            return 1+solve(node.left)+solve(node.right)
        return solve(root)