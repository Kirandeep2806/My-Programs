# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        hm = {}
        q = deque([(root, None)])

        while q:
            for i in range(len(q)):
                curr,parent = q.popleft()
                hm[curr] = parent
                if curr.left:
                    q.append((curr.left, curr))
                if curr.right:
                    q.append((curr.right, curr))
        vis = set()
        q.append(target)
        for i in range(k):
            for j in range(len(q)):
                target = q.popleft()
                vis.add(target)
                if (target in hm) and hm[target]!=None and (hm[target] not in vis):
                    q.append(hm[target])
                if target.left and (target.left not in vis):
                    q.append(target.left)
                if target.right and (target.right not in vis):
                    q.append(target.right)
        res = []
        for i in q:
            res.append(i.val)
        return res
