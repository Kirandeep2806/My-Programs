# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        hm = {}
        for i in range(n):
            hm[inorder[i]] = i

        def solve(inStart, inEnd, preStart, preEnd):
            if (inStart > inEnd) or (preStart > preEnd):
                return None
            node = TreeNode(preorder[preStart])
            node.left = solve(inStart, hm[node.val] - 1, preStart+1, preStart + hm[node.val] - inStart)
            node.right = solve(hm[node.val]+1, inEnd, preStart + hm[node.val] - inStart + 1, preEnd)
            return node

        root = solve(0, n-1, 0, n-1)
        return root
