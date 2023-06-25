# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hm = {}
        n = len(inorder)
        for i in range(n):
            hm[inorder[i]] = i
        def solve(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd or postStart < postEnd:
                return None
            node = TreeNode(postorder[postStart])
            numsLeft = hm[node.val] - inStart
            numsRight = inEnd - hm[node.val]
            node.left = solve(inStart, hm[node.val]-1, postStart-numsRight-1, postEnd)
            node.right = solve(hm[node.val]+1, inEnd, postStart-1, postStart-numsRight) # postEnd+numsLeft
            return node
        root = solve(0, n-1, n-1, 0)
        return root
