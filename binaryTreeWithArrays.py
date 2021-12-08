#!/usr/bin/env python3

import numpy as np

height = int(input("Enter the height of the tree : "))
tree = np.array([0]*(2**(height)-1), dtype=np.object)

currHeight = 0
while currHeight < height:
    start = 2**(currHeight) - 1
    end = 2**(currHeight + 1) - 2
    while start <= end:
        tree[start] = input("Enter the data into the node {} : ".format(start)) or None
        start += 1
    currHeight += 1


def preorder(root):
    try:
        if tree[root] is not None:
            print(tree[root], end=" ")
            preorder(2*root+1)
            preorder(2*root+2)
    except:
        return

def postorder(root):
    try:
        if tree[root] is not None:
            preorder(2*root+1)
            preorder(2*root+2)
            print(tree[root], end=" ")
    except:
        return

def  inorder(root):
    try:
        if tree[root] is not None:
            preorder(2*root+1)
            print(tree[root], end=" ")
            preorder(2*root+2)
    except:
        return

print("Preorder : ", end=" ")
preorder(0)
print()
print("Postorder : ", end=" ")
postorder(0)
print()
print("Inorder : ", end=" ")
inorder(0)
print()