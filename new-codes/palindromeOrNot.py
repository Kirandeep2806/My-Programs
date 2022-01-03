#!/usr/bin/env python3

# Write a program to find whether given string of characters given from keyboard is  palindrome or not. Program should store input data in both stack and queue. After entering all the characters compare content of stack and queue using pop and dequeue operations. If contents are same print that given characters are palindrome else not a palindrome.

# Note: program can ignore case of letters, blanks and punctuations.


import re


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

data = re.sub(r"[^A-Za-z0-9]", "", input("Enter a word : ").lower())
print("Input you have entered after cleaning :", data)
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
    print("It is a Palindrome!!")
else:
    print("It is not a palindrome!!")
