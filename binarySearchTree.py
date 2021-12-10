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


treeObj = BST()
while True:
    choice = int(input("1. Insert\t2. Traverse\t3. Search\t4. Exit\nEnter your choice : "))
    if choice == 1:
        data = int(input("Enter the input to be inserted : "))
        treeObj.insert(data)
    elif choice == 2:
        treeObj.traverseTree(treeObj.root)
        print()
    elif choice == 3:
        data = int(input("Enter the data to be searched : "))
        print(treeObj.search(data, treeObj.root))
    else:
        quit(0)
