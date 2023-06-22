'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        def dfs(node):
            if node is None:
                return True
            s = 0
            if node.left:
                if dfs(node.left) == False:
                    return False
                s += node.left.data
            if node.right:
                if dfs(node.right) == False:
                    return False
                s += node.right.data
            if (node.left or node.right) and node.data != s:
                return False
            return True
        return int(dfs(root))
