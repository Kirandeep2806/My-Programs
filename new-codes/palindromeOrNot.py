#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.tos = None

    def push(self, data):
        if self.tos == None:
            self.tos = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.tos
            self.tos = newNode

    def pop(self):
        if self.tos is None:
            return False
        ele = self.tos.data
        self.tos = self.tos.next
        return ele


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, data: object) -> None:
        newNode = Node(data)
        if self.front == self.rear == None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self) -> str:
        if self.front == self.rear == None:
            return False
        if self.front == self.rear:
            deletedEle = self.front.data
            self.front = self.rear = None
        else:
            deletedEle = self.front.data
            self.front = self.front.next
        return deletedEle


q = Queue()
s = Stack()

data = input("Enter a word : ")
for char in data:
    q.enqueue(char)
    s.push(char)

indicator = True
isPalindrome = True

while indicator:
    q_ele = q.dequeue()
    s_ele = s.pop()
    if q_ele != s_ele:
        isPalindrome = False
        break
    indicator = q_ele or s_ele

if isPalindrome:
    print("Palindrome!!")
else:
    print("Not a palindrome!!")
