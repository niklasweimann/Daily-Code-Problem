class Node:
    def __init__(self, value, nextNode):
        self.Value = value
        self.Next = nextNode
    def __repr__(self):
        return "<V: {} Next: {}>".format(self.Value, self.Next)

class SingleLinkedList:
    def __init__(self):
        self.Head: Node = None
        self.Size = 0

    def add(self, value):
        new_node = Node(value, self.Head) 
        self.Head = new_node 
        self.Size += 1

    def getList(self):
        res = "["
        head :Node= self.Head
        while head is not None:
            res += "{} ".format(head.Value)
            head = head.Next
        res += "]"
        res += " Size: {}".format(self.Size)
        return res

    def reverse(self):
        prev = None
        current = self.Head 
        while current is not None: 
            next = current.Next
            current.Next = prev 
            prev = current 
            current = next
        self.Head = prev 
        


l = SingleLinkedList()
l.add("A")
l.add("B")
l.add("C")
l.add("D")
l.add("E")
l.add("F")
print(l.getList())
l.reverse()
print(l.getList())
l.reverse()
print(l.getList())