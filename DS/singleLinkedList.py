

class Node:
    '''Creation of new nodes'''
    def __init__(self, data) -> None:
        self.data = data
        self.link = None


class SingleLinkedList:

    '''Operations on linked lists'''
    def __init__(self) -> None:
        self.header = None

    def takeInput(self):
        return eval(input("Enter the data : "))

    def getNode(self, position):
        count = 0
        nodeLink = self.header
        currNode = self.header
        while (not (position == count)) and nodeLink:
            count += 1
            currNode = nodeLink
            nodeLink = nodeLink.link
        return currNode


    # createNode defaults to insertion at the End of the linked list

    def createNode(self):
        newNode = Node(self.takeInput())
        if self.header is None:
            self.header = newNode
        else:
            lastNode = self.getNode(-1)
            lastNode.link = newNode
        print("Node has been created successfully!")
        

    def insertAtStart(self):
        newNode = Node(self.takeInput())
        if self.header is None:
            self.header = newNode
        else:
            newNode.link = self.header
            self.header = newNode

    def insertAtMiddle(self, pos):
        if self.header is None and pos == 0:
            newNode = Node(self.takeInput())
            self.header = newNode
        elif self.header is None:
            print("Cannot insert node")
        elif self.header is not None and pos == 0:
            newNode = Node(self.takeInput())
            newNode.link = self.header
            self.header = newNode
        else:
            newNode = Node(self.takeInput())
            positionedNode = self.getNode(pos)
            newNode.link = positionedNode.link
            positionedNode.link = newNode

    def deleteAtStart(self):
        if self.header is None:
            print("No elements are there to be deleted")
        else:
            nextNode = self.getNode(1)
            self.header = nextNode.link
            print("Node has been deleted successfully")

    def deleteAtMiddle(self, pos):
        if self.header is None:
            print("No elements are there to be deleted")
        else:
            nodeLink = self.header
            currNode = self.header
            count = 0
            while (not(count == pos)) and nodeLink:
                count += 1
                currNode = nodeLink
                nodeLink = nodeLink.link

            currNode.link = nodeLink.link

    def deleteAtEnd(self):
        if self.header is None:
            print("No elements are there to be deleted")
        else:
            nodeLink = self.header
            count = 0
            while nodeLink.link:
                count += 1
                currNode = nodeLink
                nodeLink = nodeLink.link
            if not count:
                self.header = None
            else:
                currNode.link = None
            print("Node deleted successfully at the end")


    # def updateValueAt(self, pos):
    #     pass

    def traversal(self):
        if self.header is None:
            print("No elements to be displayed")
        else:
            nodeLink = self.header
            while nodeLink:
                print(nodeLink.data)
                nodeLink = nodeLink.link

    def getValueAt(self, pos):
        if self.header is None:
            print("No data in Linked List")
        else:
            positionedNode = self.getNode(pos+1)
            print(f"Value at index {pos} is : {positionedNode.data}")
        






linkedList = SingleLinkedList()


while True:
    print("Which operation you want to perform : ")
    choice = int(input("1. Creation\n2. Insertion\n3. Deletion\n4. Updation\n5. Display\n6. Obtain value\n7. Press any other key to exit\nEnter your choice : "))

    if choice == 1:
        linkedList.createNode()

    elif choice == 2:
        subChoice = int(input("1. Insert at start\n2. Insert at middle\n3. Insert at end : "))
        if subChoice == 1:
            linkedList.insertAtStart()
        elif subChoice == 2:
            position = int(input("At which indexed node you want to insert the node : "))
            linkedList.insertAtMiddle(position)
        elif subChoice == 3:
            linkedList.createNode()
        else:
            print("Invalid Choice!")

    elif choice == 3:
        subChoice = int(input("1. Delete at start\n2. Delete at middle\n3. Delete at end : "))
        if subChoice == 1:
            linkedList.deleteAtStart()
        elif subChoice == 2:
            position = int(input("Position where you want to delete the node : "))
            linkedList.deleteAtMiddle(position)
        elif subChoice == 3:
            linkedList.deleteAtEnd()
        else:
            print("Invalid Choice!")

    elif choice == 4:
        position = int(input("Position where you want to update the node : "))
        linkedList.updateValueAt(position)

    elif choice == 5:
        linkedList.traversal()

    elif choice == 6:
        position = int(input("Which indexed node's data you want to fetch :"))
        linkedList.getValueAt(position)

    else:
        break