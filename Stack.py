class Node:
    def __init__(self,myData):
        self.prev = None
        self.data = myData
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtfirstPosition(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def traversal(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next

dll = DoublyLinkedList()
dll.insertAtfirstPosition("Rohit")
dll.insertAtfirstPosition("Mehak")
dll.traversal()
