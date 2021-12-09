#!/usr/bin/env python3

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None

    def getParentPos(self, data: int, root: Node) -> Node:
        if data < root.data:
            if root.left is None:
                return root
            else:
                return self.getParentPos(data, root.left)
        else:
            if root.right is None:
                return root
            else:
                return self.getParentPos(data, root.right)

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            pos = self.getParentPos(data, self.root)
            if data < pos.data:
                pos.left = Node(data)
            else:
                pos.right = Node(data)

    def traverseTree(self, root: Node):
        if root:
            print(root.data, end=" ")
            self.traverseTree(root.left)
            self.traverseTree(root.right)


treeObj = BST()
l = list(map(int, input("List the data of binary search tree : ").split()))
for i in l:
    treeObj.insert(i)
treeObj.traverseTree(treeObj.root)
print()
