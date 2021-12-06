#!/usr/bin/env python3

import numpy as np

class Queue:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.queue = np.array([None]*capacity)

    def enqueue(self, data: int) -> None:
        if self.front == self.rear == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = data

        elif self.rear == self.capacity - 1:
            print("Queue is full cannot insert the element!!")

        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self) -> int:
        if self.front == self.rear == -1:
            return "No elements to be deleted from the queue."

        elif self.front == self.rear:
            delElement = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            return "Deleted data is : {}".format(delElement)

        else:
            delElement = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return "Deleted data is : {}".format(delElement)

    def size(self) -> int:
        if self.rear == self.front == -1:
            return "No elements present in the queue...!"
        return "No.of elements in the queue is {}".format(self.rear - self.front + 1)

    def isEmpty(self) -> bool:
        if self.front == self.rear == -1:
            return True
        return False

    def display(self) -> None:
        ptr = self.front
        if not self.isEmpty():
            print("Data in the queue is : ", end=" ")
            while ptr <= self.rear:
                print(self.queue[ptr], end=" ")
                ptr += 1
            print()

        else:
            print("No elements to be displayed in the queue!!")


size = int(input("Enter the size of the queue : "))
q = Queue(size)

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
