class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def findIntersection(A, B):
    visitedIDs = []

    currentNode = A
    while currentNode != None:
        visitedIDs.append(id(currentNode))
        currentNode = currentNode.next

    currentNode = B
    while currentNode != None:
        currentID = id(currentNode)
        if currentID in visitedIDs:
            return currentNode
        visitedIDs.append(currentID)
        currentNode = currentNode.next

    return None


first_list = Node(1, Node(2, Node(3, Node(4))))
secont_list = Node(8, Node(9, first_list))

intersectingNode = findIntersection(first_list, secont_list)

print(intersectingNode)
