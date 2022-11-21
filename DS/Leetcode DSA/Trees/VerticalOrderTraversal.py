#!/usr/bin/python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from sys import maxsize

class Solution:
	def __init__(self):
		self.minVal = maxsize
		self.maxVal = -maxsize-1
		self.ds = [] # Format : (level, y, val)
		self.res = defaultdict(list) # Contains the value to be returned
	def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
		self.ds.append([0, 0, root])
		while self.ds:
			s = self.ds.__len__()
			self.resTemp = defaultdict(list)
			for i in range(s):
				packedData = self.ds.pop(0)
				level, y, node = packedData
				if node.left:
					self.ds.append([level+1, y-1, node.left])
				if node.right:
					self.ds.append([level+1, y+1, node.right])
				self.resTemp[y].append(node.val)
				self.minVal = min(self.minVal, y)
				self.maxVal = max(self.maxVal, y)
			for i in range(self.minVal, self.maxVal+1):
				self.res[i].extend(sorted(self.resTemp[i]))
		self.ds.clear()
		for i in range(self.minVal, self.maxVal+1):
			self.ds.append(self.res[i])
		return self.ds
