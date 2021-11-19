#!/usr/bin/env python3

class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class CLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def Insert(self):
        n = eval(input("Enter the data : "))
        newNode = Node(n)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            opt = int(input("""1. Beginning
2. Middle
3. End
Where you want to insert the data : """))
            if opt == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif opt == 2:
                pos = int(input("Enter the position of insertion : "))
                ptr = self.head
                for _ in range(pos-1):
                    ptr = ptr.next
                newNode.prev = ptr
                newNode.next = ptr.next
                ptr.next.prev = newNode
                ptr.next = newNode

            elif opt == 3:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.head.prev = newNode

    def Delete(self):
        opt = int(input("""1. Beginning
2. Middle
3. End
Where you want to insert the data : """))
        if self.head == None:
            print("No elements to be deleted")
        elif self.head == self.head.next:
            self.head = None
            self.tail = None
        elif opt == 1:
            self.head.next.prev = self.tail
            self.head = self.head.next
            self.tail.next = self.head
        elif opt == 2:
            pos = int(input("Enter the position of deletion : "))
            ptr = self.head
            for _ in range(pos-1):
                ptr = ptr.next
            ptr.next.next.prev = ptr
            ptr.next = ptr.next.next


        elif opt == 3:
            ptr = self.head
            while ptr.next != self.tail:
                ptr = ptr.next
            ptr.next = self.head
            self.tail = ptr
            self.head.prev = self.tail

    def Display(self):
        if self.head == None:
            print("No elements to be displayed")
        else:
            n = int(input("1. Forward Traversal\n2. Reverse Traversal\nEnter your choice : "))
            if n == 1:
                ptr = self.head
                while ptr.next != self.head:
                    print(ptr.data)
                    ptr = ptr.next
                print(ptr.data)
            else:
                ptr = self.tail
                while ptr.prev != self.tail:
                    print(ptr.data)
                    ptr = ptr.prev
                print(ptr.data)

    def Count(self):
        if self.head == None:
            print("0 elements")
        else:
            ptr = self.head
            count = 0
            while ptr.next != self.head:
                count += 1
                ptr = ptr.next
            count += 1
            print(count, "elements")
                

    def Search(self):
        if self.head == None:
            print("No elements to be searched")
        else:
            pos = 1
            found = False
            target = int(input("Enter the data to be searched : "))
            ptr = self.head
            while ptr.next != self.head:
                if ptr.data == target:
                    print("Element found at position", pos)
                    found = True
                ptr = ptr.next
                pos += 1
            else:
                if ptr.data == target:
                    print("Element found at position", pos)
                    found = True
            if not found:
                print("Element is not found")
            

cll = CLL()
while True:
    choice = int(input("1. Insertion\n2. Deletion\n3. Display\n4. Count\n5. Search\n6. Exit\nEnter your choice : "))
    if choice == 1:
        cll.Insert()
    elif choice == 2:
        cll.Delete()
    elif choice == 3:
        cll.Display()
    elif choice == 4:
        cll.Count()
    elif choice == 5:
        cll.Search()
    else:
        break
