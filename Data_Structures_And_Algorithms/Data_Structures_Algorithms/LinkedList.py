class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)

    def addNode(self,data):
        temp = self.head
        if temp.value == None:
            temp.value = data
        new_node= Node(data)
        while temp.next!=None:
            temp = temp.next
        temp.next = new_node

    def printList(self):
        temp = self.head
        while temp.next !=None:
            print(temp.value)
            temp = temp.next
        print(temp.value)

    def getLength(self):
        count = 0
        if self.head.value == None:
            return 0
        count+=1
        temp = self.head
        while temp.next != None:
            count+=1
            temp = temp.next
        return count

    def reverseList(self):
        if self.getLength() <= 1:
            return
        prevNode = None
        currentNode = self.head
        nextNode = self.head.next

        while currentNode.next != None:
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            nextNode = currentNode.next
        currentNode.next = prevNode
        self.head = currentNode

    def deleteTail(self):
        if self.head.value == None:
            return
        if self.head.next == None:
            self.head.value = None
            return
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
    def deleteValue(self, value):
        if self.head.value == None:
            print("This list is empty")
            return
        temp = self.head
        while temp.next != None:
            if temp.next.value == value:
                temp.next = temp.next.next
                return
            else:
                temp = temp.next
        print("We could not find this value in the list")
