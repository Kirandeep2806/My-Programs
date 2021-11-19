import numpy as np

size = int(input("Enter the size of the stack : "))

class Stack:
    def __init__(self, stackSize):
        self.tos = -1
        self.stackSize = stackSize
        self.stack = np.array([None]*size)
    
    def push(self):
        if self.tos == self.stackSize - 1:
            print("Stack Overflow")
        else:
            data = int(input("Enter the data you want to push into the stack : "))
            self.tos += 1
            self.stack[self.tos] = data

    def pop(self):
        if self.tos == -1:
            print("Stack Underflow")
        else:
            print("Poped element is :", self.stack[self.tos])
            self.stack[self.tos] = None
            self.tos -= 1
            
    def display(self):
        if self.tos == -1:
            print("No elements")
        else:
            temp = self.tos
            while temp != -1:
                print(self.stack[temp], end=" ")
                temp -= 1
            print()
        
    def peek(self):
        if self.tos == -1:
            print("No elements in the stack")
        else:
            print("Top of stack :", self.stack[self.tos])

    def isEmpty(self):
        if self.tos == -1:
            print("Stack is empty")
        else:
            print("Elements are present in the stack")


s = Stack(size)
while True:
    choice = int(input("""Operation you want to perform : 
1. Push
2. Pop
3. Display
4. Peek
5. Is Empty
6. Exit

Enter your choice : """))



    if choice == 1:
        s.push()
    if choice == 2:
        s.pop()
    if choice == 3:
        s.display()
    if choice == 4:
        s.peek()
    if choice == 5:
        s.isEmpty()
    if choice == 6:
        exit(0)

