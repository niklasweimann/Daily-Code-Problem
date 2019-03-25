class Stack:
    def __init__(self):
        self.maximum = None
        self.data = []

    def push(self, val):
        self.data.append(val)
        if self.maximum is None:
            self.maximum = val
        elif val > self.maximum:
            self.maximum = val

    def pop(self):
        if len(self.data) is 0:
            return None
        else:
            res = self.data.pop(len(self.data)-1)
            if res is self.maximum:
                if len(self.data) is 0:
                    self.maximum = None
                else:
                    self.maximum = max(self.data)
            return res

    def max(self):
        return self.maximum


# Test Code
stack = Stack()
for i in range(0, 5):
    stack.push(i)
    print("Pusing {0} to stack.".format(i))
print("Max after fill: {}".format(stack.max()))
for j in range(0, 6):
    print("Poping {0}. time. Result:{1}".format(j, stack.pop()))
print(stack.max())
