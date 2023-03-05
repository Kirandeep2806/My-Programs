# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        l=0
        q=deque([root])
        while q:
            temp=deque()
            s=0
            for i in range(len(q)):
                ele=q.popleft()
                if ele.left:
                    temp.append(ele.left)
                if ele.right:
                    temp.append(ele.right)
                s+=ele.val
            q=temp.copy()
            l+=1
            insort(arr,s)
        if k<=l:
            return arr[l-k]
        return -1
        