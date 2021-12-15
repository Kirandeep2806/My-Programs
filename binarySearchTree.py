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

    def preorder(self, root: Node) -> None:
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root: Node) -> None:
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root: Node) -> None:
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def search(self, data: int, root: Node) -> Node:
        if root:
            if data == root.data:
                return "Element {} is found".format(data)
            else:
                if data < root.data:
                    return self.search(data, root.left)
                else:
                    return self.search(data, root.right)
        return "Element {} is not present in the tree".format(data)

    def findMax(self, root: Node) -> Node:
        if root is None or root.right is None:
            return None
        self.findMax(root.right)

    def deleteNode(self, root: Node, data: int) -> Node:
        if root:
            if root.data<data:
                root.right = self.deleteNode(root.right, data)
            elif root.data>data:
                root.left = self.deleteNode(root.left, data)
            else:
                if root.left and root.right:
                    temp = self.findMax(root.left)
                    root.data = temp.data
                    root.left = self.deleteNode(root.left, temp.data)
                elif root.left:
                    root = root.left
                else:
                    root = root.right
        return root


treeObj = BST()
while True:
    choice = int(input("1. Insert\t2. Preorder Traverse\t3. Inorder Traverse\t4. Postorder Traverse\t5. Search\t6. Delete\t7. Exit\nEnter your choice : "))
    if choice == 1:
        data = int(input("Enter the input to be inserted : "))
        treeObj.insert(data)
    elif choice == 2:
        treeObj.preorder(treeObj.root)
        print()
    elif choice == 3:
        treeObj.inorder(treeObj.root)
        print()
    elif choice == 4:
        treeObj.postorder(treeObj.root)
        print()
    elif choice == 5:
        data = int(input("Enter the data to be searched : "))
        print(treeObj.search(data, treeObj.root))
    elif choice == 6:
        data = int(input("Enter the data to be deleted : "))
        treeObj.deleteNode(treeObj.root, data)
    else:
        quit(0)
