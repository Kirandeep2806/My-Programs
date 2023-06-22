# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,0)])
        maxwidth=0
        while q:
            n=len(q)
            mn=q[0][1]
            for i in range(n):
                node, cnt = q.popleft()
                cnt -= mn
                if i==0:
                    first = cnt
                if i==n-1:
                    last = cnt
                if node.left:
                    q.append((node.left,2*cnt+1))
                if node.right:
                    q.append((node.right,2*cnt+2))
            maxwidth=max(maxwidth,last-first+1)
        return maxwidth
