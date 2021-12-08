#!/usr/bin/env python3

import numpy as np

height = int(input("Enter the height of the tree : "))
MAX_NODES = 2**(height)-1
tree = np.array([None]*MAX_NODES, dtype=object)

currHeight = 0
start = 2**(currHeight) - 1
end = 2**(currHeight + 1) - 2
currPtr = 0


def updateValues() -> None:
    global currHeight, start, end, currPtr
    currHeight += 1
    start = 2**(currHeight) - 1
    end = 2**(currHeight + 1) - 2

def insert(data: object) -> None:
    global currPtr
    if currHeight < height:
        if start <= currPtr <= end:
            tree[currPtr] = data
            currPtr += 1
        else:
            updateValues()
            if currPtr < MAX_NODES:
                tree[currPtr] = data
                currPtr += 1
            else:
                print("No nodes available to insert the data")
    else:
        print("No nodes available to insert the data")

def preorder(root: int) -> None:
    try:
        if tree[root] is not None:
            print(tree[root], end=" ")
            preorder(2*root+1)
            preorder(2*root+2)
    except:
        return

def postorder(root: int) -> None:
    try:
        if tree[root] is not None:
            postorder(2*root+1)
            postorder(2*root+2)
            print(tree[root], end=" ")
    except:
        return

def  inorder(root: int) -> None:
    try:
        if tree[root] is not None:
            inorder(2*root+1)
            print(tree[root], end=" ")
            inorder(2*root+2)
    except:
        return


while True:
    choice = int(input("1. Insertion\t2. Preorder Traversal\t3. Inorder Traversal\t4. Postorder Traversal\t5. Exit\nEnter the operation : "))
    if choice == 1:
        data = input("Enter the data into the node {} : ".format(currPtr)) or None
        insert(data)
    elif choice == 2:
        print("Preorder : ", end=" ")
        preorder(0)
        print()
    elif choice == 3:
        print("Inorder : ", end=" ")
        inorder(0)
        print()
    elif choice == 4:
        print("Postorder : ", end=" ")
        postorder(0)
        print()
    else:
        exit(0)