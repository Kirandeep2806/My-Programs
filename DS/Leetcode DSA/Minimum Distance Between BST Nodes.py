# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def soln(self,root,prev,res):
        if root is None:
            return
        self.soln(root.left,prev,res)
        if prev[0]!=-1:
            res[0]=min(res[0],root.val-prev[0])
        prev[0]=root.val
        self.soln(root.right,prev,res)
        

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev=[-1]
        res=[100005]
        self.soln(root,prev,res)
        return res[0]
