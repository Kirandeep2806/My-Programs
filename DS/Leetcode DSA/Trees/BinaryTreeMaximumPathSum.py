# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]
        def compute(root, res):
            global maxVal
            if root is None:
                return 0
            lv = max(0, compute(root.left, res))
            rv = max(0, compute(root.right, res))
            res[0] = max(res[0], root.val + lv + rv)
            return root.val+max(lv,rv)
        compute(root, res)
        return res[0]
