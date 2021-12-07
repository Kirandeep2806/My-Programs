#!/usr/bin/env python3

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

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
            return "No elements to be deleted from the queue!!"
        elif self.front == self.rear:
            deletedEle = self.front.data
            self.front = self.rear = None
            return "Deleted element from the queue is {}".format(deletedEle)
        else:
            deletedEle = self.front.data
            self.front = self.front.next
            return "Deleted element from the queue is {}".format(deletedEle)

    def size(self) -> int:
        countOfElements = self.display(forSize=True)
        return countOfElements

    def isEmpty(self) -> bool:
        if self.rear == self.front == None:
            return True
        return False

    def display(self, forSize=False) -> None or bool:
        count = 0
        if not self.isEmpty():
            ptr = self.front
            if not forSize:
                print("Data in the queue is :", end=" ")
            while ptr is not None:
                if not forSize:
                    print(ptr.data, end=" ")
                else:
                    count += 1
                ptr = ptr.next
            print()

        else:
            if not forSize:
                print("No elements to be displayed!!")

        if forSize:
            return "No.of elements in the queue is : {}".format(count)
        

    
q = Queue()

while True:
    choice = int(input("""Operation you want to perform : 
1. Enqueue
2. Dequeue
3. Count of Elements
4. isEmpty
5. Display
6. Exit

Enter your choice : """))



    if choice == 1:
        data = int(input("Enter the data into the queue : ") or "100")
        q.enqueue(data)

        '''
        Get annotations like
        print(q.enqueue.__annotations__)
        '''
        
    elif choice == 2:
        data = q.dequeue()
        print(data)
    elif choice == 3:
        response = q.size()
        print(response)
    elif choice == 4:
        response = q.isEmpty()
        if response:
            print("Empty!!")
        else:
            print("Not empty!!")
    elif choice == 5:
        q.display()
    else:
        exit(0)
