# #!/usr/bin/env python3

# # A teacher noted absentees in a class and constructed binary tree  with absentees as its keys. You have to check whether a binary search tree is or not. 							CO6,BL4
# # Input :  first input will be no of vertices of a binary tree and remaining lines contains three integer values
# # key, leftchild and right child . If node does not have leftchild and rightchild will be equal to -1.
# # Also find Inorder, preorder and post order traversals for the given binary search tree

# # 3 1 2
# # 1 -1 -1
# # 2 -1 -1


dataAndAddr = {}

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Traversals:
    def __init__(self):
        self.inorderData = []
        self.preorderData = []
        self.postorderData = []

    def preorder(self, root):
        if root:
            self.preorderData.append(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorderData.append(root.data)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.postorderData.append(root.data)


n = int(input("Enter the no.of vertices : "))
root = None
for i in range(n):
    l = list(map(int, input().split()))
    if i == 0:
        dataAndAddr[l[0]] = Node(l[0])
        root = dataAndAddr[l[0]]
    if l[1] != -1:
        dataAndAddr[l[1]] = Node(l[1])
        dataAndAddr[l[0]].left = dataAndAddr[l[1]]
    if l[2] != -1:
        dataAndAddr[l[2]] = Node(l[2])
        dataAndAddr[l[0]].right = dataAndAddr[l[2]]

if not root:
    print("No data is provided")
else:
    t = Traversals()
    t.inorder(root)
    temp = t.inorderData
    if sorted(temp) == temp:
        print("It is a Binary Search Tree")
        print("Inorder :", *t.inorderData)
        t.preorder(root)
        print("Preorder :", *t.preorderData)
        t.postorder(root)
        print("Postorder :", *t.postorderData)
    else:
        print("It's not a BST")
