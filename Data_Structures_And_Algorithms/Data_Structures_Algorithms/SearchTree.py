class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data=None):
        self.head = Node(data)

    def addNode(self, value):
        newNode = Node(value)
        if self.head.value is None:
            self.head = newNode
            return
        temp = self.head
        while True:
            if newNode.value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    return
                temp = temp.left
                continue
            if newNode.value > temp.value:
                if temp.right is None:
                    temp.right = newNode
                    return
                temp = temp.right
            if newNode.value == temp.value:
                return
                continue

    def findValue(self,value):
        temp = self.head
        while True:
            if temp.value == value:
                return True
            if value < temp.value:
                if temp.left is None:
                    return False
                temp = temp.left
                continue
            if value > temp.value:
                if temp.right is None:
                    return False
                temp = temp.right
                continue

    def treeHeight(self, node):
        if node is None:
            return -1;
        else:
            leftheight = self.treeHeight(node.left)
            rightheight = self.treeHeight(node.right)
            if leftheight > rightheight:
                return leftheight + 1
            else:
                return rightheight + 1