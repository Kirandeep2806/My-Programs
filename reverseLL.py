#!/usr/bin/python3

class Node:
    def __init__(self, data) -> None:
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def insert(self, data) -> None:
        new_node = Node(data)
        new_node.data = data
        new_node.next = self.head
        self.head = new_node
    def reverse(self) -> None:
        curr = self.head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.traverse()
ll.reverse()
ll.traverse()
