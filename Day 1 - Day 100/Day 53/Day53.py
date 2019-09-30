class Stack:
    def __init__(self):
        self.data = []

    def append(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return False if self.data else True


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        while (not self.stack1.isEmpty):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(data)
        while (not self.stack2.isEmpty):
            self.stack1.append(self.stack2.pop())
        pass

    def dequeue(self):
        if self.stack1.isEmpty():
            return None
        return self.stack1.pop()


queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
print(queue.dequeue())  # A
print(queue.dequeue())  # B
print(queue.dequeue())  # None
