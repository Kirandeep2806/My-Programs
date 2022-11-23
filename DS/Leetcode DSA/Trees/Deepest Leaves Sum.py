# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Apply BFS for more efficiency


class Solution:
    def __init__(self):
        self.res = 0
    def computeHeight(self, root):
        if root is None:
            return 0
        lh = self.computeHeight(root.left)
        rh = self.computeHeight(root.right)
        return 1+max(lh, rh)
    def calculateSum(self, root, h, height=1):
        if root:
            self.calculateSum(root.left, h, height+1)
            if height==h:
                self.res += root.val
            self.calculateSum(root.right, h, height+1)
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        h = self.computeHeight(root)
        self.calculateSum(root, h, 1)
        return self.res
