class Node:
    def __init__(self, data: object) -> None:
        self.left = None
        self.data = data
        self.right = None

    def preorder(self, root) -> None:
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root) -> None:
        if root:
            self.preorder(root.left)
            self.preorder(root.right)
            print(root.data, end=" ")

    def inorder(self, root) -> None:
        if root:
            self.preorder(root.left)
            print(root.data, end=" ")
            self.preorder(root.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal  : ", end="")
root.preorder(root)

print("\nInorder traversal   : ", end="")
root.inorder(root)

print("\nPostorder traversal : ", end="")
root.postorder(root)
