class Node:
   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size+=1
        return True

    def removeNode(self,value):
        p = None
        c = self.head
        # List has only one Element
        if self.head is None:
            return
        if self.head.getNextNode() is None:
            self.head = None
            return
        while c.getNextNode():
            p = c
            c = c.getNextNode()
            if c.data is value:
                p.setNextNode(c.getNextNode())
                return


    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()

myList = LinkedList()
print('Add')
myList.addNode('a')
myList.addNode('b')
myList.addNode('c')
myList.addNode('d')
myList.addNode('e')
myList.printNode()
print('Remove')
myList.removeNode('a')
myList.removeNode('c')
myList.removeNode('e')
myList.printNode()