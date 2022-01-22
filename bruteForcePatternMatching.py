#!/usr/bin/python

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=self.rear=None
    def insert(self):
        if self.front==self.rear==None:
            key=int(input("enter the value to be inserted:"))
            newnode=Node(key)
            self.front=self.rear=newnode
        else:
            key=int(input("enter the value to be inserted "))  
            newnode=Node(key)
            newnode.next=self.front
            self.front=newnode
            
    def pop(self):
        if self.rear==self.front==None or self.front.next==None:
            print("list is empty:")
        else:
            self.front=self.front.next 
    def display(self):
        if self.front.next==None:
            print("list is empty:")
        else:
            self.ptr=self.front
            while(self.ptr==None):
               
               print(self.ptr.data)
               self.ptr=self.ptr.next
q=queue()
while(True):
    print("\tQueue Operations\n1.INSERTION\n2.DELETION\n3.DISPLAY\n4.EXIT\n")
    n=int(input("enter your choice :"))
    if n==1:
        
        q.insert()
    if n==2:
        q.pop()
    if n==3:
        q.display()
    if n==4:
        exit(0)