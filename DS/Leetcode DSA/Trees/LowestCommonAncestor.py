class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', a: 'TreeNode', b: 'TreeNode') -> 'TreeNode':
        if (root is None) or (root==a) or (root==b):
            return root
        val1=self.lowestCommonAncestor(root.left,a,b)
        val2=self.lowestCommonAncestor(root.right,a,b)
        if((val1==a and val2==b) or (val1==b and val2==a)):
            return root
        # elif(val1==a or val1==b): This condition is not valid when a root value is returned
        elif(val1!=None):
            return val1
        elif(val2!=None):
            return val2
