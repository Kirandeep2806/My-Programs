from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root:
            q=deque([root])
            while q:
                temp=deque()
                r1=[]
                while q:
                    cur=q.popleft()
                    r1.append(cur.val)
                    if cur.left is not None:
                        temp.append(cur.left)
                    if cur.right is not None:
                        temp.append(cur.right)
                q=temp.copy()
                res.append(r1)
        return res[::-1]
