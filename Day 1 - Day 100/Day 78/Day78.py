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
        head: Node = self.Head
        while head is not None:
            res += "{} ".format(head.Value)
            head = head.Next
        res += "]"
        res += " Size: {}".format(self.Size)
        return res

    def addLists(self, lists: []):
        sorted_lists = sorted(lists, key=lambda x: x.Head.Value)
        for i in sorted_lists:
            while i.Head is not None:
                head: Node = i.Head
                prev = None
                while head.Next is not None:
                    prev = head
                    head = head.Next
                self.add(head)
                if prev is not None:
                    prev.Next = None
                else:
                    i.Head = None


l = SingleLinkedList()
l.add("A")
l.add("B")
l.add("C")
k = SingleLinkedList()
k.add("D")
k.add("E")
k.add("F")
j = SingleLinkedList()
j.add("G")
j.add("H")
j.add("I")
j.add("J")
h = SingleLinkedList()
h.addLists([l, j, k])
print(h.getList())
