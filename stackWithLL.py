class Node:
    def __init__(self, data=0):
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
        if self.tos == None:
            print("Stack Underflow")
        else:
            print("Poped out element is :", self.tos.data)
            self.tos = self.tos.next

    def isEmpty(self):
        if self.tos == None:
            print("No elements in the stack")
        else:
            print("Element are present in the stack")

    def peek(self):
        if self.tos == None:
            print("No elements in the stack")
        else:
            print("Element on the top of the stack is :", self.tos.data)

    def display(self):
        if self.tos == None:
            print("No elements in the stack")
        else:
            ptr = self.tos
            print("Stack elements are : ", end=" ")
            while ptr!=None:
                print(ptr.data, end=" ")
                ptr = ptr.next
            print()



s = Stack()
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
        s.push(int(input("Enter the data you want to push into the stack : ")))
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


