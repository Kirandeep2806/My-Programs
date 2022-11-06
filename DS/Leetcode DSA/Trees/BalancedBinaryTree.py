#!/usr/bin/python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def fetchHeight(self, root) -> int:
		# if root is None:
		# 	return 0
		# lh = 1+fetchHeight(root.left)
		# rh = 1+fetchHeight(root.right)
		# return max(lh, rh)
		pass

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
			return 0
		lh = 1+fetchHeight(root.left)
		rh = 1+fetchHeight(root.right)
		if abs(lh-rh)<=1:
			return max(lh, rh)
		return False
		
