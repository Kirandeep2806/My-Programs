'''
Write a method splitStack that takes a stack of integers as a parameter and splits it into negatives 
and non-negatives. The numbers in the stack should be rearranged so that all the negatives appear 
on the bottom of the stack and all the non-negatives appear on the top. In other words, if after this 
method is called you were to pop numbers off the stack, you would first get all the nonnegative 
numbers and then get all the negative numbers. It does not matter what order the numbers appear 
in as long as all the negatives appear lower in the stack than all the non-negatives. You may use a 
single queue as auxiliary storage. 
How many stacks are needed to implement a queue. Give the implementation
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SplitStack:
    def __init__(self):
        self.header = None
        self.tail = None

    def main(self, data):
        if self.header == None:
            self.header = self.tail = Node(data)
        elif data < 0:
            newNode = Node(data)
            newNode.next = self.header
            self.header = newNode
        elif data > 0:
            newNode = Node(data)
            self.tail.next = newNode
            self.tail = newNode
        else:
            pass

    def display(self):
        ptr = self.header
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

l = list(map(int, input("Enter numbers : ").split()))
s = SplitStack()
for i in l:
    s.main(i)
s.display()